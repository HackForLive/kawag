import configparser
from datetime import date, datetime
import os
from pathlib import Path

# not used as problematic
# import plyer

from kivy.logger import Logger
from kivy.utils import platform
# from bs4 import BeautifulSoup
from requests import Response
from requests_html import HTMLSession

from db.db_engine import DbEngine


class TaskManager:
    def __init__(self, config: configparser.ConfigParser):
        self.config = config
        self.db_engine = DbEngine(sql_connection_str=
        f"sqlite:///{(Path(__file__).parent.parent).joinpath(self.config['DEFAULT']['DB_NAME'])}")


    def trigger_kaktus(self, title:str, text: str):
        self.notify(title=title, msg=text)

    def send_notification(self, title: str, message: str):
        """
        Alternative to plyer
        """
        from jnius import autoclass
        channel: str = 'kawag_01'
        Context = autoclass('android.content.Context')
        # AndroidString = autoclass('java.lang.String')
        service = autoclass('org.kivy.android.PythonService').mService

        notification_service = service.getSystemService(
            Context.NOTIFICATION_SERVICE)
        NotificationBuilder = autoclass('android.app.Notification$Builder')
        NotificationChannel = autoclass('android.app.NotificationChannel')
        Drawable = autoclass('org.test.myapp.R$drawable')
        Logger.info(dir(Drawable))
        icon = Drawable.ic_launcher
        app_context = service.getApplication().getApplicationContext()
        notification_builder = NotificationBuilder(app_context, channel)
        notification_builder.setContentTitle(title)
        notification_builder.setContentText(message)
        notification_builder.setSmallIcon(icon)
        notification_builder.setAutoCancel(True)
        new_notification = notification_builder.getNotification()

        notification_service.createNotificationChannel(
            NotificationChannel(
                channel, "notificationWorker", 3 #NotificationManager.IMPORTANCE_DEFAULT
            )
        )
        notification_service.notify(0, new_notification)


    def notify(self, title: str, msg: str) -> None:
        """
        Push notification with title and msg
        :param title: notification title
        :param msg: notification message
        """

        self.send_notification(title=title, message=msg)
        # plyer.notification.notify(title=title, message=msg, ticker='ticker', toast=True)
        Logger.info("push notification sent")

    def fetch_kaktus_dobijecka_page(self) -> Response:
        session = HTMLSession()

        return session.get(self.config['DEFAULT']['BASE_URL'])

    def parse_kaktus_content(self, response: Response) -> tuple[date, str]:
        # soup = BeautifulSoup(response.html.raw_html, 'html.parser')
        # return soup.find('div', {'class': 'box-bubble'}).find_all('p')[0].text
        prefix = 'https://www.mujkaktus.cz/api/download'
        pdf_links = [l for l in response.html.links if l.startswith(prefix)]
        the_rest_content = pdf_links[0][len(prefix):]

        raw_date = the_rest_content.split('FB_')[1].split('.pdf')[0]
        return datetime.strptime(raw_date, '%d%m%Y').date(), the_rest_content
    

    def pull_notification(self):
        received_argument = os.getenv("PYTHON_SERVICE_ARGUMENT")
        Logger.info('Tasks: argument passed to python: %s', received_argument)

        kaktus_content = self.fetch_kaktus_dobijecka_page()
        event_date, message = self.parse_kaktus_content(response=kaktus_content)

        msg = f'Dobíječka\n{datetime.strftime(event_date, "%d/%m/%Y")}'

        latest = self.db_engine.get_latest_notification()

        if not latest or latest.message != msg or event_date == date.today():
            self.db_engine.create_notification(msg=msg)
            if platform == 'android':
                self.trigger_kaktus(title="It's time!", text=msg)
        else:
            if platform == 'android':
                self.trigger_kaktus(title="Nothing yet.", text=msg)

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config_path = Path(__file__).parent.parent.joinpath('config.ini')
    config.read(config_path)

    task_manager = TaskManager(config=config)
    task_manager.pull_notification()

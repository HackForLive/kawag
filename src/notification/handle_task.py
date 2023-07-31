import configparser
import os
from pathlib import Path

# not used as problematic
# import plyer

from kivy.logger import Logger
from kivy.utils import platform
from bs4 import BeautifulSoup
from requests_html import HTMLSession

from db.manager import SqlLiteManager


def trigger_kaktus():
    text = get_kaktus_latest()
    notify(title='test', msg=text)

def send_notification(title: str, message: str):
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


def notify(title: str, msg: str) -> None:
    """
    Push notification with title and msg
    :param title: notification title
    :param msg: notification message
    """

    send_notification(title=title, message=msg)
    # plyer.notification.notify(title=title, message=msg, ticker='ticker', toast=True)
    Logger.info("push notification sent")

def get_kaktus_latest():
    session = HTMLSession()

    response = session.get(config['DEFAULT']['BASE_URL'])
    soup = BeautifulSoup(response.html.raw_html, 'html.parser')
    return soup.find('div', {'class': 'box-bubble'}).find_all('p')[0].text

if __name__ == '__main__':
    config = configparser.ConfigParser()
    Logger.info(Path(__file__).parent.parent.joinpath('config.ini'))
    config.read(Path(__file__).parent.parent.joinpath('config.ini'))

    db_manager = SqlLiteManager(db_file=(Path(__file__).parent.parent).joinpath(
            config['DEFAULT']['DB_NAME']))

    received_argument = os.getenv("PYTHON_SERVICE_ARGUMENT")
    Logger.info('Tasks: argument passed to python: %s', received_argument)

    if platform == 'android':
        trigger_kaktus()

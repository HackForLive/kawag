import configparser
from pathlib import Path
import time

import plyer
import schedule

from kivy.logger import Logger
from kivy.utils import platform
from bs4 import BeautifulSoup
from requests_html import HTMLSession

if platform == 'android':
    from jnius import autoclass

def init():
    if platform == 'android':
        package_name='org.test.myapp'
        service_name='Notificationtask'
        s_name = f'{package_name}.Service{service_name}'
        service = autoclass(s_name)
        m_activity = autoclass('org.kivy.android.PythonActivity').mActivity
        argument = ''
        service.start(m_activity, argument)

def trigger_kaktus():
    text = get_kaktus_latest()
    notify(title='test', msg=text)

def notify(title: str, msg: str) -> None:
    """
    Push notification with title and msg
    :param title: notification title
    :param msg: notification message
    """
    plyer.notification.notify(title=title, message=msg)
    Logger.info("push notification sent")

def get_kaktus_latest():
    session = HTMLSession()

    response = session.get(config['DEFAULT']['BASE_URL'])
    soup = BeautifulSoup(response.html.raw_html, 'html.parser')
    return soup.find('div', {'class': 'box-bubble'}).find_all('p')[0].text


# schedule.every(2).minutes.do(trigger_kaktus)
config = configparser.ConfigParser()
config.read(Path(__file__).parent.parent.parent.joinpath('config.ini'))

while True:
    schedule.run_pending()
    time.sleep(1)

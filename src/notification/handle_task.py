import configparser
import os
from pathlib import Path

import plyer

from kivy.logger import Logger
from bs4 import BeautifulSoup
from kivy.utils import platform
from requests_html import HTMLSession


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

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read(Path(__file__).parent.parent.parent.joinpath('config.ini'))

    received_argument = os.getenv("PYTHON_SERVICE_ARGUMENT")
    Logger.info('Tasks: argument passed to python: {0}'.format(received_argument))

    if platform == 'android':
        trigger_kaktus()

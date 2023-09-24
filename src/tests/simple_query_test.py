import configparser
from pathlib import Path

from requests_html import HTMLSession

config = configparser.ConfigParser()
config.read(Path(__file__).parent.parent.joinpath('config.ini'))

session = HTMLSession()

r = session.get(config['DEFAULT']['BASE_URL'])

box = r.html.find('.box-bubble', first=True).find('p', first=True)
print(box.text)

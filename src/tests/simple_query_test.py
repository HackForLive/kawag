import configparser

from requests_html import HTMLSession

config = configparser.ConfigParser()
config.read('config.ini')

session = HTMLSession()

r = session.get(config['DEFAULT']['BASE_URL'])

box = r.html.find('.box-bubble', first=True).find('p', first=True)
print(box.text)

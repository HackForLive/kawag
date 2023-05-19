import os
import random
import configparser

from requests_html import HTMLSession
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class KaktusUI(BoxLayout):
    def __init__(self):
        super(KaktusUI, self).__init__()

    def generate_number(self):
        self.random_label.text = get_kaktus_latest()#str(random.randint(0,100 ))    


class Kaktus(App):
    def build(self):
        return KaktusUI()

def get_kaktus_latest():
    config = configparser.ConfigParser()
    config.read('config.ini')
    session = HTMLSession()

    response = session.get(config['DEFAULT']['BASE_URL'])

    return response.html.find('.box-bubble', first=True).find('p', first=True).text

if __name__ == "__main__":
    Kaktus().run()

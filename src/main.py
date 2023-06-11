from pathlib import Path
import sqlite3
import configparser

from requests_html import HTMLSession
from kivy.lang import Builder
from kivymd.app import MDApp
from db.manager import SqlLiteManager

config = configparser.ConfigParser()
config.read((Path(__file__).parent).parent.joinpath('config.ini'))

class Kaktus(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.db_manager = SqlLiteManager(db_file=config['DEFAULT']['DB_NAME'])

    def generate_number(self):
        self.random_label.text = get_kaktus_latest()

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        self.db_manager.create_connection()

        return Builder.load_file('kaktus.kv')

    def submit(self):
        text = self.root.ids.word_input.text
        text = get_kaktus_latest()
        self.db_manager.insert_new_record(notification=text)
        # Add a little message
        self.root.ids.word_label.text = f'{text} Added'
        # Clear the input box
        self.root.ids.word_input.text = ''

    def show_records(self):
        records = self.db_manager.get_all_record()

        word = ''
        # Loop thru records
        for record in records:
            word = f'{word}\n{record[0]}'
            self.root.ids.word_label.text = f'{word}'

def get_kaktus_latest():
    session = HTMLSession()

    response = session.get(config['DEFAULT']['BASE_URL'])

    return response.html.find('.box-bubble', first=True).find('p', first=True).text

if __name__ == "__main__":
    Kaktus().run()

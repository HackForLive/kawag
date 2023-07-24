from pathlib import Path
import os
import configparser

from kivy.lang import Builder
from kivy.utils import platform
from kivymd.app import MDApp

from src.db.manager import SqlLiteManager

config = configparser.ConfigParser()
config.read(Path(__file__).parent.joinpath('config.ini'))

class Kaktus(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.db_manager = SqlLiteManager(db_file=(Path(__file__).parent).joinpath(
            config['DEFAULT']['DB_NAME']))
        self.db_manager.create_notification_table()
        if platform == 'android':
            from src.notification.scheduled_task import schedule_task
            schedule_task(minutes=2)

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        self.db_manager.create_connection()

        return Builder.load_file(os.path.join('src', 'kaktus.kv'))

    def submit(self):
        text = self.root.ids.word_input.text
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

if __name__ == "__main__":
    Kaktus().run()

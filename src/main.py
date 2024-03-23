from pathlib import Path
import configparser

from kivy.lang import Builder
from kivy.utils import platform
from kivymd.app import MDApp
from kivymd.uix.behaviors.toggle_behavior import MDToggleButton
from kivymd.uix.button import MDFlatButton


from db.db_engine import DbEngine

config = configparser.ConfigParser()
config.read(Path(__file__).parent.joinpath('config.ini'))


class MyToggleButton(MDFlatButton, MDToggleButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.background_down = self.theme_cls.primary_color

class Kaktus(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if platform == 'android':
            from notification.scheduled_task import schedule_task
            schedule_task()

        self._db_engine = DbEngine(
        sql_connection_str=
        f"sqlite:///{(Path(__file__).parent).joinpath(config['DEFAULT']['DB_NAME'])}")

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"

        return Builder.load_file('kaktus.kv')

    def submit(self):
        text = self.root.ids.word_input.text
        self._db_engine.create_notification(msg=text)
        # Add a little message
        self.root.ids.word_label.text = f'{text} Added'
        # Clear the input box
        self.root.ids.word_input.text = ''

    def show_latest_records(self):
        latest = self._db_engine.get_latest_notification()
        if latest:
            self.root.ids.word_label.text = latest.message
        else:
            self.root.ids.word_label.text = ''

if __name__ == "__main__":
    Kaktus().run()

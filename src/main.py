from pathlib import Path
from datetime import datetime
import configparser

from kivy.clock import Clock
from kivy.lang import Builder
from kivy.utils import platform
from kivymd.app import MDApp
from kivymd.uix.behaviors.toggle_behavior import MDToggleButton
from kivymd.uix.button import MDFlatButton
from kivy.logger import Logger

from kivy.core.text import LabelBase

LabelBase.register(name="UbuntuMono", fn_regular="fonts/UbuntuMono-Regular.ttf")


from db.db_engine import DbEngine

config = configparser.ConfigParser()
config.read(Path(__file__).parent.joinpath('config.ini'))

if platform == "android":
    from jnius import autoclass, cast
    from android.permissions import request_permissions, Permission, check_permission

    def ask_notification_permission():
        if not check_permission(Permission.POST_NOTIFICATIONS):
            request_permissions([Permission.POST_NOTIFICATIONS])
else:
    def ask_notification_permission():
        pass


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
        Clock.schedule_interval(lambda dt: self.check_db_value(), 30)  # every 20 seconds
    
    def on_start(self):
        Clock.schedule_once(lambda dt: ask_notification_permission(), 10)


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

    def enable_or_disable_notification(self, *args):
        Logger.info(args)
        sc = self.root.ids.seg_options

        # sci_off = self.root.ids.sci_off
        sci_on = self.root.ids.sci_on
        if sc.current_active_segment == sci_on:
            Logger.info("enabled")
            if platform == 'android':
                from notification.scheduled_task import schedule_task
                schedule_task()
            else:
                from notification.handle_task import TaskManager
                tm = TaskManager(config=config)
                msg_date, msg=tm.parse_kaktus_content(response=tm.fetch_kaktus_dobijecka_page())
                Logger.info(msg=msg)
                message = f'Dobíječka\n{datetime.strftime(msg_date, "%d/%m/%Y")}'
                self._db_engine.create_notification(msg=message)
        else:
            Logger.info("disabled")
            if platform == 'android':
                from notification.scheduled_task import cancel_task
                cancel_task()

    def check_db_value(self):
        latest = self._db_engine.get_latest_notification()
        Logger.info(f'latest: {latest}')
        if latest:
            self.root.ids.message_label.text = latest.message

if __name__ == "__main__":
    Kaktus().run()
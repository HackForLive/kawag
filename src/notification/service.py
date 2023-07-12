from kivy.utils import platform
from kivy.logger import Logger
import plyer


class NotificationService:
    def __init__(self) -> None:
        if platform == 'android':
            from jnius import autoclass
            package_name='org.test.myapp'
            service_name='Notification'
            s_name = f'{package_name}.Service{service_name}'
            service = autoclass(s_name)
            m_activity = autoclass('org.kivy.android.PythonActivity').mActivity
            argument = ''
            service.start(m_activity, argument)
            # service.mService.setAutoRestartService(True)

            # service = autoclass('org.test.myapp.Notification')
            # m_activity = autoclass('org.kivy.android.PythonActivity').mActivity
            # argument = ''
            # service.start(m_activity, argument)
            # Logger.info("service started")

    def notify(self, title: str, msg: str) -> None:
        """
        Push notification with title and msg
        :param title: notification title
        :param msg: notification message
        """
        plyer.notification.notify(title=title, message=msg)
        Logger.info("push notification sent")

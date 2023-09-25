import unittest
from src.db.db_engine import DbEngine


class TestKaktusRegex(unittest.TestCase):

    def setUp(self) -> None:
        self._db_engine = DbEngine(sql_connection_str="sqlite://")
        return super().setUp()

    def test_latest_notification(self):
        latest = self._db_engine.get_latest_notification()
        self.assertTrue(expr=latest is None, msg='Nothing is stored in db.')

        self._db_engine.create_notification(msg='msg1')
        self._db_engine.create_notification(msg='msg2')

        latest = self._db_engine.get_latest_notification()

        self.assertTrue(expr=latest and hasattr(latest, 'message'), msg='Notification exists.')
        self.assertTrue(expr=latest.message == 'msg2', msg='Notification message is the latest.')

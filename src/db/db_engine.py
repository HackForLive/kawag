from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.model.notification import Notification, base


class DbEngine:
    def __init__(self, sql_connection_str: str) -> None:
        self._engine = create_engine(sql_connection_str, echo=True)

        # create db and tables
        base.metadata.create_all(self._engine)
        self._session = sessionmaker(bind=self._engine)

    def create_notification(self, msg: str) -> None:
        """
        :param msg: message
        """
        session = self._session()
        notification = Notification(message=msg, created_at=datetime.utcnow())
        session.add(notification)
        session.commit()
        session.close()

    # def get_notification_by_date(self, date_param: date) -> Notification:
    #     session = self._session()
    #     record = session.query(Notification).filter(
    #         Notification.created_at == date_param
    #         ).first()
    #     return record

    def get_latest_notification(self) -> Notification:
        session = self._session()
        res = session.query(Notification).order_by(Notification.created_at.desc()).all()
        session.close()
        return res[0] if res else None

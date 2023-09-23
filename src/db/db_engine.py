from typing import List

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from db.model.notification import Notification, base

class DbEngine:
    def __init__(self, db_file_path) -> None:
        self._engine = create_engine(f"sqlite:///{db_file_path}", echo=True)

        # create db and tables
        base.metadata.create_all(self._engine)
        self._session = sessionmaker(bind=self._engine)

    def create_notification(self, msg: str) -> None:
        """
        :param msg: message
        """
        session = self._session()
        notification = Notification(message=msg)
        session.add(notification)
        session.commit()
        session.close()

    def get_all_notifications(self) -> List[Notification]:
        session = self._session()
        return session.query(Notification).all()

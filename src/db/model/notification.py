from sqlalchemy import String, Integer, Column, DateTime, Boolean
# from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.declarative import declarative_base


base = declarative_base()


class Notification(base):
    __tablename__ = 'notification'
    id = Column(Integer, primary_key=True)
    # message: Mapped[str] = mapped_column(String(100))
    message = Column(String(length=200))
    created_at = Column(DateTime)

    def __repr__(self) -> str:
        return f"Notification(id={self.id!r}, message={self.message!r})"

class NotificationStatus(base):
    __tablename__ = 'notification_status'
    id = Column(Integer, primary_key=True)
    enabled = Column(Boolean)

    def __repr__(self) -> str:
        return f"NotificationStatus(id={self.id!r}, enabled={self.enabled!r})"

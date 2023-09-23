from sqlalchemy import String, Integer, Column
# from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.declarative import declarative_base


base = declarative_base()


class Notification(base):
    __tablename__ = 'notification'
    id = Column(Integer, primary_key=True)
    # message: Mapped[str] = mapped_column(String(100))
    message = Column(String(100))

    def __repr__(self) -> str:
        return f"Notification(id={self.id!r}, message={self.message!r})"

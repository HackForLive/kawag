from sqlalchemy import String, Integer, Column, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column


Base = declarative_base()
# The echo=True parameter indicates that SQL emitted by connections will be logged to standard out.
engine = create_engine("sqlite://", echo=True)


class Notification(Base):
    __tablename__ = 'notification'
    id = Column(Integer, primary_key=True)
    message: Mapped[str] = mapped_column(String(100))

    def __repr__(self) -> str:
        return f"Notification(id={self.id!r}, message={self.message!r})"

Base.metadata.create_all(engine)
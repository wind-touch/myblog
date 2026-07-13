from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String


class Base(DeclarativeBase):
    pass


class Test(Base):
    __tablename__ = "test"

    id = Column(Integer,
                primary_key=True,
                autoincrement=True)
    message = Column(String(200),
                     nullable=False)
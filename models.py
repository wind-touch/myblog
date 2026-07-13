from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id = Column(Integer,
                primary_key=True,
                autoincrement=True)
    username = Column(String(50),
                      nullable=False,
                      unique=True)
    hashed_password = Column(String,
                             nullable=False)

# Native Imports
from sqlalchemy import Column, Integer, String

# Created Imports
from database.database import ModelBase


class User(ModelBase):
    __tablename__ = 'tbusers'

    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_name = Column(String, unique=True, nullable=False)
    user_password = Column(String, nullable=False)
    user_email = Column(String, unique=True, nullable=False)
    user_token = Column(String, nullable=True)
    user_status = Column(Integer, nullable=False)
    user_last_modification_user_id = Column(Integer, nullable=False)

    def __repr__(self) -> str:
        return f'User(id={self.user_id}, username={self.user_name})'

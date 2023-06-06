import uuid
from sqlalchemy import Column, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID

Base = declarative_base()

class Users(Base):
    __tablename__ = "users"

    id = Column(String(36), primary_key=True, default=str(uuid.uuid4()))
    email = Column(String, unique=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)

    def __init__(self, id, email, password, is_active):
        self.id = id
        self.email = email
        self.password = password
        self.is_active = is_active

    def __repr__(self):
        return f"<User(id={self.id}, " \
               f"email=\"{self.email}\", " \
               f"password=\"{self.password}\", " \
               f"is_active={self.is_active})>"

import uuid
from sqlalchemy import Column, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID

Base = declarative_base()

class Users(Base):
    __tablename__ = "users"

    id = Column(String(36), primary_key=True, default=str(uuid.uuid4()))
    email = Column(String, unique=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    def __init__(self, email, hashed_password, is_active):
        self.email = email
        self.hashed_password = hashed_password
        self.is_active = is_active

    def __repr__(self):
        return f"<User(id={self.id}, " \
               f"email=\"{self.email}\", " \
               f"hashed_password=\"{self.hashed_password}\", " \
               f"is_active={self.is_active})>"

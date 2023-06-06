from typing import List, Optional

from pydantic import BaseModel, Field

class UserBase(BaseModel):
    email: str
    is_active: bool


class UserCreate(UserBase):
    password: str
    pass


class User(UserBase):
    id: str

    class Config:
        orm_mode = True

class UserUpdate(BaseModel):
    password: Optional[str] = Field(None, title='Password', description='Optional password')
    is_active: Optional[bool] = Field(None, title='Is Active', description='Optional active status')
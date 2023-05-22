from typing import List, Optional

from pydantic import BaseModel

class UserBase(BaseModel):
    id: Optional[str] = None
    email: str
    hashed_password: str
    is_active: bool


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: str

    class Config:
        orm_mode = True
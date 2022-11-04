from typing import Optional

from pydantic import BaseModel, EmailStr
from .base import DatabaseBase


class UserBase(BaseModel):
    email: EmailStr
    name: str
    phone: str


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    email: Optional[EmailStr]
    name: Optional[str]
    phone: Optional[str]
    password: Optional[str]


class UserInDBBBase(UserBase, DatabaseBase):
    pass


class User(UserInDBBBase):
    pass


class UserInDB(UserInDBBBase):
    password: str

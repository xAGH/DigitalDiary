from pydantic import BaseModel
from .base import DatabaseBase
from typing import Optional


class ContactBase(BaseModel):
    name: str
    phone: str


class ContactCreate(ContactBase):
    pass


class ContactUpdate(BaseModel):
    name: Optional[str]
    phone: Optional[str]


class ContactInDB(ContactBase, DatabaseBase):
    user_id: int


class Contact(ContactInDB):
    pass

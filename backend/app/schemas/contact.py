from pydantic import BaseModel
from .base import DatabaseBase
from typing import Optional

class ContactCreate(BaseModel):
    name: str
    phone: str
    user_id: int

class ContactUpdate(BaseModel):
    name: Optional[str]
    phone: Optional[str]


class ContactInDB(ContactCreate, DatabaseBase):
    pass


class Contact(ContactInDB):
    pass

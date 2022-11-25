from http import HTTPStatus
from typing_extensions import TypeVarTuple
from pydantic import BaseModel
from typing import Optional, Any
from app.schemas.contact import Contact

from app.schemas.user import User

response_type = str | User | Contact | list[Contact | None] | None


class ResponseSchema(BaseModel):
    status: bool = True
    message: Optional[str] = None
    body: response_type = None

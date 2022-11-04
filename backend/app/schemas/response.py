from http import HTTPStatus
from pydantic import BaseModel
from typing import Optional, Any


class ResponseSchema(BaseModel):
    status: bool = True
    message: Optional[str] = None
    body: Optional[Any] = None

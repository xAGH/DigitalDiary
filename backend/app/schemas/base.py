from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class DatabaseBase(BaseModel):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

    class Config:
        orm_mode = True

from datetime import datetime

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base():
    id = Column(Integer, primary_key=True)
    created_at = Column(String, nullable=False, default=datetime.now())
    updated_at = Column(String, nullable=True)
    deleted_at = Column(String, nullable=True)

    __table_args__ = {'extend_existing': True}
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower() + "s"

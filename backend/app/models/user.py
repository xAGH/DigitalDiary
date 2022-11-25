from app.db.base_class import Base

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(Base):   # type: ignore
    email = Column(String(100), nullable=False)
    name = Column(String(length=100), nullable=False)
    phone = Column(String(length=15), nullable=False)
    password = Column(String, nullable=False)
    contacts = relationship("Contact", back_populates="user")

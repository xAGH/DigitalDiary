from app.db.base_class import Base

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Contact(Base):  # type: ignore
    name = Column(String(length=100))
    phone = Column(String(length=15))
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="contacts")

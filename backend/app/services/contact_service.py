from app.models.contact import Contact
from app.services.base import CRUDBase
from app.schemas.contact import ContactCreate, ContactUpdate

from fastapi import Depends
from fastapi.encoders import jsonable_encoder

from sqlalchemy.orm import Session


class CRUDContact(CRUDBase[Contact, ContactCreate, ContactUpdate]):

    def create_contact(
        self,
        contact: ContactCreate,
        user_id: int,
        db: Session
    ) -> Contact:
        contact = jsonable_encoder(contact)
        db_contact = self.model(**contact, user_id=user_id)
        db.add(db_contact)
        db.commit()
        db.refresh(db_contact)
        return db_contact

    def get_contacts(
        self,
        *,
        user_id: int,
        skip: int = 0,
        limit: int = 100,
        db: Session
    ) -> list[Contact | None]:
        return (
            db.query(self.model)
            .filter(Contact.user_id == user_id)
            .offset(skip)
            .limit(limit)
            .all()
        )


contact = CRUDContact(model=Contact)

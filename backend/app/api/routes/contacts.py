from http import HTTPStatus
from app.models import User
from fastapi import Response
from app.schemas import ContactCreate, ContactUpdate, ResponseSchema
from app.api.dependencies import get_current_user, get_db
from app.services import contact as contact_service

from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

router = APIRouter()

not_found: ResponseSchema = ResponseSchema(
    status=False,
    message="Contact not found"
)


@router.get("/", response_model=ResponseSchema)
def read_contacts(
    res: Response,
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> ResponseSchema:

    if isinstance(current_user, tuple):
        res.status_code = current_user[0]
        return current_user[1]

    return ResponseSchema(
        body=contact_service.get_contacts(
            user_id=current_user.id,
            skip=skip,
            limit=limit,
            db=db
        )
    )


@router.post("/", response_model=ResponseSchema)
def create_contact(
    res: Response,
    body: ContactCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
) -> ResponseSchema:

    if isinstance(current_user, tuple):
        res.status_code = current_user[0]
        return current_user[1]

    return ResponseSchema(
        body=contact_service.create_contact(
            contact=body,
            user_id=current_user.id,
            db=db
        ))


@router.put("/{id}", response_model=ResponseSchema)
def update_contact(
    res: Response,
    id: int,
    body: ContactUpdate,
    db: Session = Depends(get_db),
) -> ResponseSchema:

    db_contact = contact_service.get(id=id, db=db)

    if db_contact is None:
        res.status_code = HTTPStatus.NOT_FOUND
        return not_found

    return ResponseSchema(body=contact_service.update(db_model=db_contact, model=body, db=db))


@router.get("/{id}", response_model=ResponseSchema)
def read_contact(
    id: int,
    db: Session = Depends(get_db)
) -> ResponseSchema:

    contact = contact_service.get(id=id, db=db)

    if contact is None:
        return not_found

    return ResponseSchema(body=contact)


@router.delete("/{id}", response_model=ResponseSchema)
def delete_contact(
    id: int,
    db: Session = Depends(get_db),
) -> ResponseSchema:

    contact = contact_service.get(id=id, db=db)

    if contact is None:
        return not_found

    return ResponseSchema(body=contact_service.remove(id=id, db=db))

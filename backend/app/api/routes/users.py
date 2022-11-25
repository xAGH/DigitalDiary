from http import HTTPStatus
from app.models import User as UserModel
from app.services import user as user_service
from app.schemas import User, UserCreate, UserUpdate
from app.schemas.response import ResponseSchema
from app.api.dependencies import get_current_user, get_db

from fastapi import APIRouter, Depends, Response

from sqlalchemy.orm import Session

router = APIRouter()

not_found: ResponseSchema = ResponseSchema(
    status=False,
    message="The user with this email already exists."
)


@router.get("/", response_model=ResponseSchema)
def get_user(
    res: Response,
    current_user: UserModel = Depends(get_current_user),
) -> ResponseSchema:

    if isinstance(current_user, tuple):
        res.status_code = current_user[0]
        return current_user[1]

    return ResponseSchema(
        status=True,
        body=current_user
    )


@router.post("/", response_model=ResponseSchema)
def create_user(
    res: Response,
    body: UserCreate,
    db: Session = Depends(get_db)
) -> ResponseSchema:

    user = user_service.get_by_email(email=body.email, db=db)

    if user is not None:
        res.status_code = HTTPStatus.CONFLICT
        return ResponseSchema(
            status=False,
            message="The user with this email already exists."
        )

    return ResponseSchema(
        body=user_service.create(user=body, db=db)
    )


@router.put("/", response_model=ResponseSchema)
def update_user(
    res: Response,
    body: UserUpdate,
    current_user: UserModel = Depends(get_current_user),
    db: Session = Depends(get_db)
) -> ResponseSchema:

    if isinstance(current_user, tuple):
        res.status_code = current_user[0]
        return current_user[1]

    user = user_service.get(id=current_user.id, db=db)

    if user is None:
        res.status_code = HTTPStatus.NOT_FOUND
        return not_found

    return ResponseSchema(
        body=user_service.update(to_update=user, user=body, db=db))


@router.delete("/", response_model=ResponseSchema)
def delete_user(
        res: Response,
        user: UserModel = Depends(get_current_user),
        db: Session = Depends(get_db)
) -> ResponseSchema:

    if isinstance(user, tuple):
        res.status_code = user[0]
        return user[1]

    user = user_service.get(id=user.id, db=db)

    if user is None:
        res.status_code = HTTPStatus.NOT_FOUND
        return not_found

    res.status_code = HTTPStatus.NO_CONTENT
    user_service.remove(id=user.id, db=db)
    return ResponseSchema()

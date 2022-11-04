from http import HTTPStatus
from app.core import security
from app.schemas import ResponseSchema
from app.core.config import settings
from app.api.dependencies import get_db
from app.services import user as user_service

from fastapi import APIRouter, Depends, Response
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/login", response_model=ResponseSchema)
def login_access_token(
    res: Response,
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
) -> ResponseSchema:

    user = user_service.authenticate(
        email=form_data.username,
        password=form_data.password,
        db=db
    )

    if not user:
        res.status_code = HTTPStatus.UNAUTHORIZED
        return ResponseSchema(
            status=False,
            message="Incorrect email or password"
        )

    if user.deleted_at is not None:
        res.status_code = HTTPStatus.FORBIDDEN
        return ResponseSchema(
            status=False,
            message=f"The user was deleted at {user.deleted_at}"
        )

    return ResponseSchema(
        status=True,
        body=settings.TOKEN_TYPE + " " + security.create_access_token(user.id)
    )

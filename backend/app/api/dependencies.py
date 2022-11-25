from http import HTTPStatus
from app.models import User
from app.schemas import ResponseSchema
from app.core.config import settings
from app.db.session import SessionLocal
from app.core.security import ALGORITHM
from app.services import user as user_service


from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from jose.exceptions import JWTError
from jose.jwt import decode as jwt_decode

from pydantic import ValidationError

from sqlalchemy.orm import Session

from typing import Generator

oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_VERSION}/login", auto_error=False
)


def get_db() -> Generator:
    try:
        db: Session = SessionLocal()
        yield db
    finally:
        db.close()  # type: ignore


def get_current_user(
    token: str = Depends(oauth2),
    db: Session = Depends(get_db)
) -> User | tuple[int, ResponseSchema]:

    if token is None:
        return HTTPStatus.UNAUTHORIZED, ResponseSchema(
            status=False,
            message="Not authenticated",
        )

    try:
        payload = jwt_decode(
            token, settings.SECRET_KEY, algorithms=[ALGORITHM]
        )

    except (JWTError, ValidationError):

        return HTTPStatus.UNAUTHORIZED, ResponseSchema(
            status=False,
            message="The token is expired or invalid",
        )

    user = user_service.get(id=payload.get("sub"), db=db)  # type: ignore

    if user is None:
        return HTTPStatus.NOT_FOUND, ResponseSchema(
            status=False,
            message="User not found"
        )

    return user

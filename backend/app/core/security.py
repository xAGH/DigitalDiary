from datetime import datetime, timedelta
from typing import Any
from jose import jwt
from passlib.context import CryptContext
from core.config import settings

crypt = CryptContext(schemes=["bcrypt"], deprecated="auto")


ALGORITHM = "HS256"


def create_access_token(
    subject: str | Any
) -> str:
    expire = datetime.utcnow() + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def verify_password(plain_password: str, hashed_password: str | bytes | None) -> bool:
    return crypt.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return crypt.hash(password)

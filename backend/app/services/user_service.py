from app.models.user import User
from app.services.base import CRUDBase
from app.core.security import get_password_hash
from app.schemas.user import UserCreate, UserUpdate
from app.core.security import get_password_hash, verify_password

from typing import Any, Dict, Optional

from sqlalchemy.orm import Session


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):

    def get_by_email(self,  email: str, db: Session) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()

    def create(self, user: UserCreate, db: Session) -> User:
        user.password = get_password_hash(user.password)
        return super().create(model=user, db=db)

    def update(
            self,
            *,
            to_update: User,
            user: UserUpdate | Dict[str, Any],
            db: Session
    ) -> User:

        if not isinstance(user, dict):
            user = user.dict(exclude_unset=True)

        if user.get("password") is not None:
            user["password"] = get_password_hash(user["password"])

        return super().update(db_model=to_update, model=user, db=db)

    def authenticate(self, email: str, password: str, db: Session) -> Optional[User]:
        user = self.get_by_email(db=db, email=email)
        if not user:
            return None
        if not verify_password(password, str(user.password)):
            return None
        return user


user = CRUDUser(model=User)

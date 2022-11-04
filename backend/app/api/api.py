from fastapi import APIRouter

from app.api.routes import auth_router, contacts_router, users_router

router = APIRouter()

router.include_router(auth_router, tags=["auth"])
router.include_router(users_router, prefix="/users", tags=["users"])
router.include_router(contacts_router, prefix="/contacts", tags=["contacts"])

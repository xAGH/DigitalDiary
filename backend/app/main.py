from api.api import router
from db.session import init_database
from core.config import settings

from fastapi import FastAPI

from starlette.middleware.cors import CORSMiddleware


app = FastAPI()

# Set all CORS enabled origins
if settings.ALLOWED_CORS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_CORS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

app.include_router(router=router, prefix=settings.API_VERSION)

init_database()

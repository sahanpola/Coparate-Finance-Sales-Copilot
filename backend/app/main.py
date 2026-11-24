from fastapi import FastAPI
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.exceptions import RequestValidationError

from app.core.config import settings
from app.core.logging_config import configure_logging
from app.core.exception_handlers import (
    http_exception_handler,
    validation_exception_handler,
    unexpected_exception_handler,
)
from app.api.v1.router import api_router


configure_logging()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Enterprise Finance and Sales Intelligence API",
)

app.include_router(
    api_router,
    prefix=settings.api_prefix,
)

app.add_exception_handler(
    StarletteHTTPException,
    http_exception_handler,
)

app.add_exception_handler(
    RequestValidationError,
    validation_exception_handler,
)

app.add_exception_handler(
    Exception,
    unexpected_exception_handler,
)


@app.get("/", tags=["Root"])
def root():
    return {
        "application": settings.app_name,
        "status": "running",
        "version": settings.app_version,
    }
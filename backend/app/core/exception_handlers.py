import logging 

from fastapi import HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

logger = logging.getLogger(__name__)

async def http_exception_handler(request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": {
                "code": "HTTP_ERROR",
                "message": str(exc.detail),
                "details": [],
            }
        },
    )


async def validation_exception_handler(
    request,
    exc: RequestValidationError,
):
    details = []

    for error in exc.errors():
        location = error.get("loc", ())

        field = ".".join(
            str(item)
            for item in location
            if item not in ("body", "query", "path", "header")
        )

        details.append(
            {
                "field": field or "request",
                "message": error["msg"],
            }
        )

    return JSONResponse(
        status_code=422,
        content={
            "error": {
                "code": "VALIDATION_ERROR",
                "message": "Request validation failed.",
                "details": details,
            }
        },
    )


async def unexpected_exception_handler(request, exc: Exception):
    logger.exception(
        "Unexpected error while processing %s %s",
        request.method,
        request.url.path,
    )

    return JSONResponse(
        status_code=500,
        content={
            "error": {
                "code": "INTERNAL_SERVER_ERROR",
                "message": "An unexpected error occurred.",
                "details": [],
            }
        },
    )



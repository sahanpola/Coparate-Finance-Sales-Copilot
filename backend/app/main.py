from fastapi import FastAPI

from app.core.config import settings
from app.api.v1.router import api_router

app = FastAPI(
    title= settings.app_name,
    version= settings.app_version,
    description="Enterprise Finance and Sales Intelligence API",
)


@app.get("/")
def root():
    return {
        "application": "Corporate Finance & Sales Intelligence Copilot",
        "status": "running",
        "version": "0.1.0",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
    }
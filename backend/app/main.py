from fastapi import FastAPI

app = FastAPI(
    title="Corporate Finance & Sales Intelligence Copilot",
    description="Enterprise Finance and Sales Intelligence API",
    version="0.1.0",
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
from pydantic import BaseModel 

class HealthResponse(BaseModel):
    status: str

class SystemInfoResponse(BaseModel):
    application: str
    version: str
    environment: str 


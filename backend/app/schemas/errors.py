from typing import Any 
from pydantic import BaseModel, Field

class ErrorDetails(BaseModel):
    field: str
    message: str

class ErrorBody(BaseModel):
    code: str
    message: str
    details: list[ErrorDetails] = Field(default_factory=list)

class ErrorResponse(BaseModel):
    error: ErrorBody
    
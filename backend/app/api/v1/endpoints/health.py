from fastapi import APIRouter 

from app.schemas.system import HealthResponse 
from app.services.system_service import SystemService 

router = APIRouter() 

@router.get("/health",
            response_model=HealthResponse,
            tags=["System"]
)

def health_check():
    return SystemService.get_health_status()



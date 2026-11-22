from fastapi import APIRouter

from app.schemas.system import SystemInfoResponse
from app.services.system_service import SystemService   

router = APIRouter()

@router.get("/system-info",
            response_model=SystemInfoResponse,
            tags=["System"]

)
def get_system_info():
    return SystemService.get_system_info()



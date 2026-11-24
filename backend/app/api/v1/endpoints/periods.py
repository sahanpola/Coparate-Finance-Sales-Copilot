from fastapi import APIRouter, Depends

from app.api.dependencies import get_period_service 
from app.schemas.period import PeriodRequest, PeriodSummary
from app.services.period_service import PeriodService

router = APIRouter()

@router.post(
    "/period/validate",
    response_model=PeriodSummary,
    tags=["Reporting"],
)
def validate_reporting_period(
    request: PeriodRequest,
    service: PeriodService = Depends(get_period_service), 
) -> PeriodSummary:
    return service.validate_period(request)


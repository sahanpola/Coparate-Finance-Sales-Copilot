import logging 

from app.schemas.period import PeriodRequest, PeriodSummary 

logger = logging.getLogger(__name__) 

class PeriodService:

    def validate_period(self,request: PeriodRequest) -> PeriodSummary:
        inclusive_days = (
            request.end_date - request.start_date  
        ).days + 1

        logger.info(
            "Validated reporting period: %s to %s" ,
            request.start_date,
            request.end_date
        )

        return PeriodSummary(
            start_date=request.start_date,
            end_date=request.end_date,
            inclusive_days=inclusive_days
        )
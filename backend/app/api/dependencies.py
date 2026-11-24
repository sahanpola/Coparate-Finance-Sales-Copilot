from app.services.period_service import PeriodService 

def get_period_service() -> PeriodService:
    return PeriodService()
from app.core.config import settings 

class SystemService:

    @staticmethod
    def get_system_info() -> dict:
        return{
            "application" : settings.app_name,
            "version" : settings.app_version,
            "environment" : settings.environment

        }

    @staticmethod
    def get_health_status() -> dict:
        return {
            "status": "healthy"
        }



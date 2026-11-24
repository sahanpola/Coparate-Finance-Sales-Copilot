from datetime import date

from pydantic import BaseModel, model_validator


class PeriodRequest(BaseModel):
    start_date: date
    end_date: date

    @model_validator(mode="after")
    def validate_date_range(self) -> "PeriodRequest":
        if self.start_date > self.end_date:
            raise ValueError(
                "Start date must be before or equal to end date."
            )

        return self


class PeriodSummary(BaseModel):
    start_date: date
    end_date: date
    inclusive_days: int
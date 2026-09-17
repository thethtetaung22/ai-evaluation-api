from datetime import datetime

from pydantic import BaseModel, Field


class EvaluationRequest(BaseModel):
    prompt: str = Field(min_length=1, max_length=10_000)
    model: str = Field(min_length=1, max_length=100)


class EvaluationResponse(BaseModel):
    id: str
    prompt: str
    model: str
    status: str
    created_at: datetime

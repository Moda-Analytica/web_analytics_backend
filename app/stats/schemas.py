from typing import Optional

from pydantic import BaseModel, Field


class MetricSchema(BaseModel):
    metric: str = Field(...)
    description: str = Field(...)
    sector: str = Field(...)
    value_type: str = Field(...)
    reference: str = Field(...)


def response_model(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def error_response_model(error, code, message):
    return {"error": error, "code": code, "message": message}

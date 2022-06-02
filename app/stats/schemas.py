from typing import Optional

from pydantic import BaseModel, Field
from bson import ObjectId


class SectorSchema(BaseModel):
    id: int = Field(..., alias="_id")
    name: str = Field(...)
    description: str = Field(...)


class SubSectorSchema(BaseModel):
    id: str = Field(..., alias="_id")
    metric: str = Field(...)
    description: str = Field(...)
    sector: str = Field(...)
    value_type: str = Field(...)
    reference: str = Field(...)
    report: str = Field(...)


    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


def response_model(data, message):
    return {
        "data": data,
        "code": 200,
        "message": message,
    }


def error_response_model(error, code, message):
    return {"error": error, "code": code, "message": message}

from pydantic import BaseModel, Field
from bson import ObjectId


class SubSectorSchema(BaseModel):
    id: str = Field(..., alias="_id")
    metric: str = Field(...)
    description: str = Field(...)
    sector: str = Field(...)
    value_type: str = Field(...)
    reference: str = Field(...)
    report: str = Field(...)
    year: str = Field(...)
    value: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

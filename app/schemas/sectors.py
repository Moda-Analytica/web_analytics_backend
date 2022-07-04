from pydantic import BaseModel, Field


class SectorSchema(BaseModel):
    id: int = Field(..., alias="_id")
    name: str = Field(...)
    description: str = Field(...)

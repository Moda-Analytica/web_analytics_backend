from pydantic import BaseModel, Field


class InfographicSchema(BaseModel):
    sector: str = Field(...)
    title: str = Field(...)
    description: str = Field(...)
    report: str = Field(...)

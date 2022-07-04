from pydantic import BaseModel, Field
from bson import ObjectId


class RunInstanceSchema(BaseModel):
    id: str = Field(..., alias="_id")
    metrics_added: int = Field(...)
    sectors_added: int = Field(...)
    start_run_time: str = Field(...)
from fastapi import APIRouter


from .database import retrieve_metrics
from .schemas import (MetricSchema, response_model, error_response_model)


router = APIRouter()


@router.get("/", response_description="Stats retrieved")
async def get_stats():
    stats = await retrieve_metrics()
    if stats:
        return response_model(stats, "Stats retrieved")
    return response_model(stats, "Empty stats returned")

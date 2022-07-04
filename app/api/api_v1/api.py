from fastapi import APIRouter

from .endpoints.sectors import router as SectorRouter
from .endpoints.infographics import router as InfographicRouter



router = APIRouter()

router.include_router(SectorRouter)
router.include_router(InfographicRouter)
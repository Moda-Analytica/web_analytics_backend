from fastapi import APIRouter

from .endpoints.sectors import router as SectorRouter
from .endpoints.infographics import router as InfographicRouter
from .endpoints.subsectors import router as SubsectorRouter


router = APIRouter()

router.include_router(SectorRouter)
router.include_router(InfographicRouter)
router.include_router(SubsectorRouter)




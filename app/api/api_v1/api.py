from fastapi import APIRouter

from .endpoints.sectors import router as SectorRouter
from .endpoints.infographics import router as InfographicRouter
from .endpoints.subsectors import router as SubsectorRouter
from .endpoints.push_notification import router as PushNotificationRouter


router = APIRouter()

router.include_router(SectorRouter)
router.include_router(InfographicRouter)
router.include_router(SubsectorRouter)
router.include_router(PushNotificationRouter)



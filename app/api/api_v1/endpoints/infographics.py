from typing import List

from fastapi import APIRouter, Depends


from ....crud.infographics import get_all_infographics

from ....db.mongodb import AsyncIOMotorClient, get_database
from ....schemas.infographics import InfographicSchema

router = APIRouter()



@router.get("/infographics", response_model=List[InfographicSchema])
async def get_infographics(db: AsyncIOMotorClient = Depends(get_database)):
    return await get_all_infographics(db)

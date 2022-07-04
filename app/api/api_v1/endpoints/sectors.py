from typing import List

from fastapi import APIRouter, Depends


from ....core.utils import create_aliased_response



from ....crud.sectors import get_all_sectors
from ....db.mongodb import AsyncIOMotorClient, get_database
from ....schemas.sectors import SectorSchema




router = APIRouter()


@router.get("/", response_description="All sectors.",  response_model=List[SectorSchema])
async def get_sectors(db: AsyncIOMotorClient = Depends(get_database)):
    return await get_all_sectors(db)
    




# @router.get("/{sector_id}/sub-sectors", response_description="Sub sectors for specified sector",
#             response_model=List[SubSectorSchema])
# async def get_sub_sectors(sector_id: str):
#     query = {"sector": sector_id}
#     stats = await sub_sector_collection.find(query).to_list(None)
#     if stats is not None and stats != []:
#         return stats
#     raise HTTPException(
#         status_code=404, detail=f"Sub sectors not found for {sector_id} sector.")


# @router.get("/{sector_id}/{sub_sector_id}", response_description="Metrics retrieved for sub sector",
#             response_model=SubSectorSchema)
# async def get_metric_for_sub_sector(sector_id: str, sub_sector_id: str):
#     if (stat := await sub_sector_collection.find_one({"_id": sub_sector_id, "sector": sector_id})) is not None:
#         return stat
#     raise HTTPException(
#         status_code=404, detail=f"Stat {sub_sector_id} was not found under {sector_id}")


# @router.get("/search", response_model=List[SubSectorSchema])
# async def search_metric(q: Optional[str] = None):
#     query = {"$search": q}
#     stats = await sub_sector_collection.find({"$text": query}).to_list(None)
#     if stats is not None and stats != []:
#         return stats
#     elif stats == []:
#         return []


# @router.get("/total_stats")
# async def total_stats():
#     run_instance_collection = db["run_instance"]
#     info = await run_instance_collection.find().limit(1).sort([('$natural', -1)]).to_list(None)

#     if info:
#         return info[0]

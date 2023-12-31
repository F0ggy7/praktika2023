from fastapi import APIRouter
from services.data_regions import get_region_all as RegionService

router = APIRouter()

@router.get('/fedresurs/regions', description='Get data about id regions')
async def regions():
    regions_data = await RegionService()
    return (regions_data)
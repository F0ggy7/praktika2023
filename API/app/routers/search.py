from fastapi import APIRouter, Query
from services.data_search import get_data_search 

router = APIRouter()

@router.get('/fedresurs/search')
async def get_search(types: int = Query(..., gt=0, le=2), searchString: str = "", isActiveLegalCase: str = 'null', regionId: str = ""):
    data = await get_data_search(types, searchString, isActiveLegalCase, regionId)
    return data

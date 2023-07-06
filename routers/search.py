from fastapi import APIRouter, Query
from services.data_search import get_data_search 

router = APIRouter()

@router.get('/fedresurs/search', description='Get bankrupt information')
async def get_search(types: int = Query(..., gt=0, le=2, description='Specify the type of person or company(2 or 1)'), searchString: str = Query("", description='Specify what query to search for') , isActiveLegalCase: str = Query("null", description='Indicate the status of the case (true, false, null) Default is null'), regionId: str = Query("",description="You can specify a region ID")):
    data = await get_data_search(types, searchString, isActiveLegalCase, regionId)
    return data

from fastapi import APIRouter
from services.info_entity import info_for_type_entity as InfoEntityService

router = APIRouter()

@router.get('/fedresurs/info/entity')
async def regions():
    type_entity = await InfoEntityService()
    return (type_entity)
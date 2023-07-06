from fastapi import APIRouter
from services.info_entity import info_for_type_entity as InfoEntityService

router = APIRouter()

@router.get('/fedresurs/info/entity', description='Get information about the type of bankruptcy')
async def info_type_entity():
    type_entity = await InfoEntityService()
    return (type_entity)
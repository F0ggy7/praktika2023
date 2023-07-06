import uvicorn

from fastapi import FastAPI

from routers import regions as RegionRouter
from routers import search as SearchRouter
from routers import entity as EntityRouter



app = FastAPI(
    title="FedresursApi"
)


app.include_router(EntityRouter.router)
app.include_router(RegionRouter.router)
app.include_router(SearchRouter.router)


if __name__ == '__main__':
    uvicorn.run("main:app",workers=1, host='0.0.0.0', port = 8000, reload=True)
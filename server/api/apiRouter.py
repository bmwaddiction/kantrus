from fastapi import APIRouter
from api.user import userApi

apiRouter = APIRouter()
apiRouter.include_router(
    userApi.router,
    prefix="/user",
    tags=["Users"]
)
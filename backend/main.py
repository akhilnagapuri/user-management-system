from fastapi import FastAPI
from core.database import database
from routers.user_router import router as user_router
from routers.auth_router import router as auth_router
app = FastAPI()

app.include_router(user_router)
app.include_router(auth_router)


@app.get("/")
async def home():
    return {
        "message": "UMS Backend Running Successfully"
    }



@app.get("/test")
async def home():

    collections = await database.list_collection_names()

    return {
        "message": "UMS Backend Running",
        "collections": collections
    }
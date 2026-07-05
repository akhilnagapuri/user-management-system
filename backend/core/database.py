from motor.motor_asyncio import AsyncIOMotorClient

from core.config import (
    MONGO_URI,
    DATABASE_NAME
)

client = AsyncIOMotorClient(MONGO_URI)

database = client[DATABASE_NAME]

users_collection = database["users"]
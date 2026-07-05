from core.database import users_collection
from bson import ObjectId


async def get_user_by_email(email: str):
    return await users_collection.find_one(
        {"email": email}
    )

async def create_user(user_data: dict):
    return await users_collection.insert_one(
        user_data
    )

async def get_all_users():
    
    users = []

    cursor = users_collection.find(
        {"is_deleted": False}
    )

    async for user in cursor:

        user["_id"] = str(user["_id"])

        users.append(user)

    return users

async def count_users():

    return await users_collection.count_documents(
        {
            "is_deleted": False
        }
    )

async def get_user_by_id(
    user_id: str
):

    return await users_collection.find_one(
        {
            "_id": ObjectId(user_id)
        }
    )
    
async def update_user(
    user_id: str,
    user_data: dict
):

    return await users_collection.update_one(
        {
            "_id": ObjectId(user_id)
        },
        {
            "$set": user_data
        }
    )

async def soft_delete_user(
    user_id: str
):

    return await users_collection.update_one(
        {
            "_id": ObjectId(user_id)
        },
        {
            "$set": {
                "is_deleted": True
            }
        }
    )

async def get_deleted_users():

    return await users_collection.find(
        {
            "is_deleted": True
        }
    ).to_list(
        length=None
    )

async def restore_user(
    user_id: str
):

    return await users_collection.update_one(
        {
            "_id": ObjectId(user_id)
        },
        {
            "$set": {
                "is_deleted": False
            }
        }
    )

async def search_users(
    query: str
):

    return await users_collection.find(
        {
            "is_deleted": False,
            "$or": [
                {
                    "username": {
                        "$regex": query,
                        "$options": "i"
                    }
                },
                {
                    "email": {
                        "$regex": query,
                        "$options": "i"
                    }
                },
                {
                    "domain": {
                        "$regex": query,
                        "$options": "i"
                    }
                },
                {
                    "mobile_number": {
                        "$regex": query,
                        "$options": "i"
                    }
                }
            ]
        }
    ).to_list(
        length=None
    )
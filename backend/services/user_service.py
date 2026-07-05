from repositories.user_repository import (
    get_user_by_email,
    create_user,
    get_all_users
)
from repositories.user_repository import (
    get_user_by_id
)

from repositories.user_repository import (
    update_user,
    get_user_by_id,
    get_user_by_email
)

from core.security import (
    hash_password
)

from repositories.user_repository import (
    soft_delete_user
)

from repositories.user_repository import (
    get_deleted_users
)

from repositories.user_repository import (
    restore_user
)

from repositories.user_repository import (
    search_users
)
from core.security import hash_password


async def create_user_service(user):
    
    existing_user = await get_user_by_email(
        user.email
    )

    if existing_user:
        return {
            "success": False,
            "message": "Email already exists"
        }

    user_data = {
    "username": user.username,
    "email": user.email,
    "domain": user.domain,
    "mobile_number": user.mobile_number,
    "password": hash_password(user.password),
    "role": user.role,
    "is_deleted": False
}

    result = await create_user(
        user_data
    )

    return {
        "success": True,
        "message": "User created successfully",
        "id": str(result.inserted_id)
    }


async def get_all_users_service():

    users = await get_all_users()

    cleaned_users = []

    for user in users:

        cleaned_users.append({
    "id": str(user["_id"]),
    "username": user["username"],
    "email": user["email"],
    "mobile_number": user.get("mobile_number", ""),
    "domain": user.get("domain", ""),
    "role": user["role"],
    "is_deleted": user["is_deleted"]
})

    return cleaned_users

async def get_current_user_service(
    current_user
):

    return {
        "id": str(current_user["_id"]),
        "username": current_user["username"],
        "email": current_user["email"],
        "role": current_user["role"]
    }


async def get_user_by_id_service(
    user_id: str
):

    user = await get_user_by_id(
        user_id
    )

    if not user:

        return {
            "success": False,
            "message": "User Not Found"
        }

    return {
        "id": str(user["_id"]),
        "username": user["username"],
        "email": user["email"],
        "mobile_number": user.get(
            "mobile_number",
            ""
        ),
        "domain": user.get(
            "domain",
            ""
        ),
        "role": user["role"]
    }

async def update_user_service(
    user_id: str,
    user
):

    existing_user = await get_user_by_id(
        user_id
    )

    if not existing_user:

        return {
            "success": False,
            "message": "User Not Found"
        }

    user_data = {
        "username": user.username,
        "email": user.email,
        "mobile_number": user.mobile_number,
        "domain": user.domain,
        "role": user.role
    }

    if user.password:

        user_data["password"] = hash_password(
            user.password
        )

    await update_user(
        user_id,
        user_data
    )

    return {
        "success": True,
        "message": "User Updated Successfully"
    }

async def soft_delete_user_service(
    user_id: str
):

    existing_user = await get_user_by_id(
        user_id
    )

    if not existing_user:

        return {
            "success": False,
            "message": "User Not Found"
        }

    await soft_delete_user(
        user_id
    )

    return {
        "success": True,
        "message": "User Deleted Successfully"
    }

async def get_deleted_users_service():

    users = await get_deleted_users()

    cleaned_users = []

    for user in users:

        cleaned_users.append({
            "id": str(user["_id"]),
            "username": user["username"],
            "email": user["email"],
            "mobile_number": user.get(
                "mobile_number",
                ""
            ),
            "domain": user.get(
                "domain",
                ""
            ),
            "role": user["role"],
            "is_deleted": user["is_deleted"]
        })

    return cleaned_users

async def restore_user_service(
    user_id: str
):

    existing_user = await get_user_by_id(
        user_id
    )

    if not existing_user:

        return {
            "success": False,
            "message": "User Not Found"
        }

    await restore_user(
        user_id
    )

    return {
        "success": True,
        "message": "User Restored Successfully"
    }

async def search_users_service(
    query: str
):

    users = await search_users(
        query
    )

    cleaned_users = []

    for user in users:

        cleaned_users.append({
            "id": str(user["_id"]),
            "username": user["username"],
            "email": user["email"],
            "mobile_number": user.get(
                "mobile_number",
                ""
            ),
            "domain": user.get(
                "domain",
                ""
            ),
            "role": user["role"],
            "is_deleted": user["is_deleted"]
        })

    return cleaned_users
from fastapi import APIRouter
from fastapi import Query
from schemas.user_schema import UserCreate
from repositories.user_repository import (
    count_users
)
from services.user_service import (
    create_user_service,
    get_all_users_service,
    get_current_user_service
)

from fastapi import Depends

from core.dependencies import (
    get_current_user,
    require_roles
)

from services.user_service import (
    get_user_by_id_service
)

from schemas.user_schema import (
    UserUpdate
)

from services.user_service import (
    update_user_service
)
from services.user_service import (
    soft_delete_user_service
)

from services.user_service import (
    get_deleted_users_service
)

from services.user_service import (
    restore_user_service
)

from services.user_service import (
    search_users_service
)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

from fastapi import HTTPException

@router.post("/setup-admin")
async def setup_admin(
    user: UserCreate
):

    total_users = await count_users()

    if total_users > 0:

        raise HTTPException(
            status_code=400,
            detail="Admin already exists"
        )

    if user.role != "admin":

        raise HTTPException(
            status_code=400,
            detail="First user must be admin"
        )

    return await create_user_service(
        user
    )

@router.post("/")
async def create_user(
    user: UserCreate,
    current_user=Depends(
        require_roles(
            ["admin", "manager"]
        )
    )
):

    return await create_user_service(user)

@router.get("/")
async def get_users(
    current_user=Depends(
        get_current_user
    )
):

    return await get_all_users_service()

@router.get("/me")
async def get_me(
    current_user=Depends(
        get_current_user
    )
):

    return {
        "username": current_user["username"],
        "email": current_user["email"],
        "role": current_user["role"]
    }

@router.get("/trash")
async def get_deleted_users_route(
    current_user=Depends(
        require_roles(
            ["admin", "manager"]
        )
    )
):

    return await get_deleted_users_service()

@router.get("/search")
async def search_users_route(
    query: str = Query(...),
    current_user=Depends(
        get_current_user
    )
):

    return await search_users_service(
        query
    )
    
@router.get("/{user_id}")
async def get_user(
    user_id: str,
    current_user=Depends(
        get_current_user
    )
):

    return await get_user_by_id_service(
        user_id
    )

@router.put("/{user_id}")
async def update_user_route(
    user_id: str,
    user: UserUpdate,
    current_user=Depends(
        require_roles(
            ["admin", "manager"]
        )
    )
):

    return await update_user_service(
        user_id,
        user
    )

@router.delete("/{user_id}")
async def delete_user(
    user_id: str,
    current_user=Depends(
        require_roles(
            ["admin"]
        )
    )
):

    return await soft_delete_user_service(
        user_id
    )

@router.put("/restore/{user_id}")
async def restore_user_route(
    user_id: str,
    current_user=Depends(
        require_roles(
            ["admin"]
        )
    )
):

    return await restore_user_service(
        user_id
    )

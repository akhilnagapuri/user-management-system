from fastapi import (
    APIRouter,
    Depends
)

from schemas.auth_schema import LoginRequest

from services.auth_service import (
    login_service
)

from core.dependencies import (
    get_current_user
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/login")
async def login(
    login_data: LoginRequest
):

    return await login_service(
        login_data.email,
        login_data.password
    )


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
from repositories.user_repository import (
    get_user_by_email
)

from core.security import (
    verify_password
)

from core.auth import (
    create_access_token
)

async def login_service(email: str, password: str):

    user = await get_user_by_email(email)

    if user and user.get("is_deleted"):

        return {
            "success": False,
            "message": "User account is inactive"
        }

    if not user:
        return {
            "success": False,
            "message": "Invalid Credentials"
        }

    if not verify_password(
        password,
        user["password"]
    ):
        return {
            "success": False,
            "message": "Invalid Credentials"
        }

    access_token = create_access_token(
        {
            "sub": user["email"],
            "role": user["role"]
        }
    )

    return {
        "success": True,
        "access_token": access_token,
        "token_type": "bearer",
        "role": user["role"]
    }
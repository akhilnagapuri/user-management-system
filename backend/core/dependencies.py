from fastapi import Depends
from fastapi.security import HTTPBearer

security = HTTPBearer()

from fastapi import HTTPException

from core.auth import (
    verify_access_token
)

from repositories.user_repository import (
    get_user_by_email
)

#async def get_current_user(
 #   token: str = Depends(oauth2_scheme)
#):

   
async def get_current_user(
    credentials = Depends(security)
):

    token = credentials.credentials

    payload = verify_access_token(
       token
    )

    if not payload:

        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )

    email = payload.get("sub")

    user = await get_user_by_email(
        email
    )

    if not user:

        raise HTTPException(
            status_code=401,
            detail="User Not Found"
        )

    return user

def require_roles(allowed_roles: list):

    async def role_checker(
        current_user=Depends(get_current_user)
    ):

        if current_user["role"] not in allowed_roles:

            raise HTTPException(
                status_code=403,
                detail="Access Denied"
            )

        return current_user

    return role_checker
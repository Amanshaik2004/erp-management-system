from fastapi import Depends, HTTPException

from services.security_service import get_current_user


def require_role(required_role: str):

    def permission(
        current_user=Depends(get_current_user)
    ):

        if current_user.role.role_name != required_role:

            raise HTTPException(
                status_code=403,
                detail="Access Denied"
            )

        return current_user

    return permission
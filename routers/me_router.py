from fastapi import APIRouter, Depends

from dependencies.auth_dependency import get_current_user

router = APIRouter(prefix="/me", tags=["User Logged"])


@router.get("/")
def me(user_id: int = Depends(get_current_user)):
    return {"user_id": user_id}

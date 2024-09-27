# user.py
from fastapi import APIRouter, Depends
from core.db.handler import get_user_by_id, create_user
from core.util.security import get_current_user

user_router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(get_current_user)],
)


@user_router.get("/{user_id}")
async def read_user(user_id: int):
    """
    Endpoint to retrieve user information by ID.
    """
    user = get_user_by_id(user_id)
    return user


@user_router.post("/")
async def create_new_user(user_data: dict):
    """
    Endpoint to create a new user.
    """
    user = create_user(user_data)
    return user

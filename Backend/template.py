# template.py
from fastapi import APIRouter, Depends
from core.db.handler import get_template_by_id, create_template
from core.util.security import get_current_user

template_router = APIRouter(
    prefix="/templates",
    tags=["templates"],
    dependencies=[Depends(get_current_user)],
)


@template_router.get("/{template_id}")
async def read_template(template_id: int):
    """
    Endpoint to retrieve template information by ID.
    """
    template = get_template_by_id(template_id)
    return template


@template_router.post("/")
async def create_new_template(template_data: dict):
    """
    Endpoint to create a new template.
    """
    template = create_template(template_data)
    return template

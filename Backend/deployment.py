# deployment.py
from fastapi import APIRouter, Depends
from core.openstack.wrapper import deploy_vm
from core.util.security import get_current_user

deployment_router = APIRouter(
    prefix="/deployments",
    tags=["deployments"],
    dependencies=[Depends(get_current_user)],
)


@deployment_router.post("/")
async def create_deployment(deployment_data: dict):
    """
    Endpoint to deploy a new VM using OpenStack.
    """
    vm_info = deploy_vm(deployment_data)
    return vm_info

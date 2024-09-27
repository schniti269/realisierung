# core/openstack/wrapper.py
from .connection import get_openstack_connection


def deploy_vm(deployment_data: dict):
    """
    Deploys a virtual machine using OpenStack SDK.
    """
    conn = get_openstack_connection()
    image = conn.compute.find_image(deployment_data["image_name"])
    flavor = conn.compute.find_flavor(deployment_data["flavor_name"])
    network = conn.network.find_network(deployment_data["network_name"])

    server = conn.compute.create_server(
        name=deployment_data["vm_name"],
        image_id=image.id,
        flavor_id=flavor.id,
        networks=[{"uuid": network.id}],
    )
    server = conn.compute.wait_for_server(server)
    return server

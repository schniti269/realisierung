# core/openstack/connection.py
import openstack


def get_openstack_connection():
    """
    Establishes a connection to the OpenStack environment.
    Replace the placeholder values with actual credentials.
    """
    conn = openstack.connect(
        auth_url="https://your-openstack-auth-url",
        project_name="your-project-name",
        username="your-username",
        password="your-password",
        user_domain_name="default",
        project_domain_name="default",
    )
    return conn

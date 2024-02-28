from resource_operation.config import subscription_id, client_id, client_secret, tenant_id
from azure.identity import ClientSecretCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.resource import SubscriptionClient
from azure.mgmt.compute import ComputeManagementClient

credential = ClientSecretCredential(tenant_id=tenant_id, client_id=client_id, client_secret=client_secret)

def get_resource_management_client():
    resource_management_client = ResourceManagementClient(credential, subscription_id)
    return resource_management_client

def get_compute_management_client():
    compute_management_client = ComputeManagementClient(credential, subscription_id)
    return compute_management_client
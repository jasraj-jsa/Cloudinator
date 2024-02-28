from resource_operation.authenticate import get_resource_management_client, get_compute_management_client
import logging

client = get_resource_management_client()
compute_client = get_compute_management_client()

logging.basicConfig(filename="cloudinator.log", format='%(asctime)s %(message)s ', filemode='w')
logger = logging.getLogger()


#function to delete multiple resources
# """
#     resource delete is a list of dictionalry containing resource id and resource group name
#     for e.g. 

#     [{"resource_id": "/subscriptions/0fee9a15-8774-4097-a3ec-07f63b029db0/resourceGroups/azure-learn-group/providers/Microsoft.Compute/virtualMachines/vm1","group_name":"azure-learn-group"}]
# """
# def delete_multiple_resource(resources_delete):
#     try:
#         for item in resources_delete:
#             api_version = client._get_api_version(item['resource_id'])
#             delete_async_operation = client.resources.begin_delete_by_id(item["resource_id"], api_version)
#             delete_async_operation.wait()
#     except Exception as e:
#         logger.error(e)

#function to delete single operation at a time
def delete_resource_by_id(resource_id):
    try :
        api_version = client._get_api_version(resource_id)
        delete_async_operation = client.resources.begin_delete_by_id(resource_id, api_version )
        return delete_async_operation
    except Exception as e:
        return 

#function to move any resources from one resource 
"""
 resource_id is the list of resourceID
 for e.g:
     resource_id = ["/subscriptions/0fee9a15-8774-4097-a3ec-07f63b029db0/resourceGroups/azure-learn-group/providers/Microsoft.Web/serverFarms/ASP-cloudinatortestres-acc7", resource_id = ["/subscriptions/0fee9a15-8774-4097-a3ec-07f63b029db0/resourceGroups/azure-learn-group/providers/Microsoft.Web/serverFarms/ASP-cloudinatortestres-acc7"]]
"""
def move_resources(resource_id, source_resource_group_name, target_resource_group_id):
    parameters = {"targetResourceGroup": target_resource_group_id, "resources":resource_id}
    try :
        move_azure_async = client.resources.begin_move_resources(source_resource_group_name, parameters)
        return move_azure_async
    except Exception as e:
        logger.error(e)
        return

#function to delete resources which are not delteable
def not_deletable_resources(source_resource_group_name, resource_id):
    create_async_operation = client.resource_groups.create_or_update("azure-delete-group",{"location":"Central India","tags":{"Owner": "Akhilesh.Kumar"}})
    create_async_operation.wait()
    target_resource_group_id = create_async_operation.id
    parameters = {"targetResourceGroup": target_resource_group_id, "resources":resource_id}
    move_azure_async = client.resources.begin_move_resources(source_resource_group_name, parameters)
    move_azure_async.wait()
    delte_async_operation = client.resource_groups.begin_delete("azure-delete-group")
    delte_async_operation.wait()
    
#to delete resource group
def delete_resource_groups(group_name):
    try:
        delte_async_operation = client.resource_groups.begin_delete(group_name)
        return delte_async_operation
    except Exception as e:
        logger.error(e)
        return

#get resource list of a resource group
def get_resource_list(group_name):
    return client.resources.list_by_resource_group(group_name)


def check_existence_by_id(resource_id, api_version):
    client.resources.check_existence_by_id(resource_id, api_version)


def validate_move_resources(resource_id, source_resource_group_name, target_resource_group_name):
    parameters = {"targetResourceGroup": target_resource_group_name, "resources":resource_id}
    client.resources.begin_validate_move_resources(source_resource_group_name, parameters)

def create_resource_groups(group_name, tags):
    create_async_operation = client.resource_groups.create_or_update(group_name, tags)
    return create_async_operation


def deallocate_vm(group_name, vm_name):
    async_vm_dealloacte = compute_client.virtual_machines.begin_deallocate(group_name, vm_name)
    async_vm_dealloacte.wait()
    

def stop_vm(group_name, vm_name):
    async_stop_vm = compute_client.virtual_machines.begin_power_off(group_name, vm_name)
    async_stop_vm.wait()

def delete_vm(group_name, vm_name):
    async_delete_vm = compute_client.virtual_machines.begin_delete(group_name, vm_name)
    async_delete_vm.wait()
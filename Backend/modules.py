from search_module.main import search_resource_by_owner_rest
from cost_management.main import cost_analysis
from metrics.main import metric
from activity_log.main import activity_log
from resource_operation.main import delete_resources_main
from data_ingestion.main import *
from utils import create_entity
from notify_users.main import send_mail,gen_email_format

table_name = "Cloudinator_Production"
def searchDB(inputUser):
    table_service = make_connection()
    return list(get_entities(table_name,table_service, "PartitionKey eq '" + inputUser + "'"))

def refreshDB(inputUser):
    resources = search_resource_by_owner_rest(inputUser)
    table_service = make_connection()
    for resource in resources:
        # print(resource)
        resourceURI = resource["id"]
        owner = resource['owner']
        if(not(resourceURI) or not(owner)):
            continue
        ent = False
        get_ents = list(get_entities(table_name,table_service,"resourceId eq '" + resourceURI + "'"))
        if(len(get_ents)):
            ent = get_ents[0]
        if(ent):
            entity = create_entity(ent["RowKey"],owner)
        else:    
            entity = create_entity(resourceURI,owner)

        # Details
        # print(resource)
        entity["resourceId"] = resourceURI
        entity["owner"] = owner
        if("name" in resource and resource["name"]!=""):
            entity["resourceName"] = resource["name"]
        if("type" in resource and resource["type"]!=""):
            entity["resourceType"] = resource["type"]
        if("kind" in resource and resource["kind"]!=""):
            entity["resourceKind"] = resource["kind"]
        if("location" in resource and resource["location"]!=""):
            entity["resourceLocation"] = resource["location"]
        entity["subscriptionName"] = resource["subscriptionName"]
        entity["resourceGroup"] = resource["resourceGroup"]
        if(not(ent) or "resourceStatus" not in ent):
            entity["resourceStatus"] = "Active"

        
        # Activity Logs
        recent_users = activity_log(resourceURI,owner)
        entity["recentUser1"] = recent_users[0]
        entity["recentUser2"] = recent_users[1]
        if(not(ent) or "oldResourceGroup" not in ent):
            entity["oldResourceGroup"] = ""

        # Cost Management
        usage_cost_USD = cost_analysis(resourceURI)
        entity["UsageCostUSD"] = usage_cost_USD

        # Metrics
        utilization = metric(resourceURI)
        if(utilization):
            entity["CPU-Utilization"] = utilization

        # Add/Modify the entity in the table
        # print(entity)
        insert_or_merge_entity(table_name,table_service,entity)

def deallocate_resource(resourceId,resourceGroup,owner):
    output = delete_resources_main(resourceId,resourceGroup,owner)
    result = output[0]
    # print(result)
    if(not(result) or "deletable" not in result or "new_resource_grp_name" not in result):
        return False
    table_service = make_connection()
    entity = create_entity(resourceId,owner)
    if(result["deletable"]):
        status = "Deallocated"
    else:
        status = "Moved"
    entity["resourceStatus"] = status
    if(not(result["deletable"])):
        entity["oldResourceGroup"] = resourceGroup
        entity["resourceGroup"] = result["new_resource_grp_name"]
    # print(entity)
    insert_or_merge_entity(table_name,table_service,entity)
    return True

def notify_users(user1,user2,owner,resourceName,resourceType,subscriptionName,resourceStatus,resourceGroup, old_resource_group):
    if((user1 and user1!="") or (user2 and user2!="")):
        send_mail(owner,gen_email_format(user1,user2),resourceName,resourceType,subscriptionName,resourceStatus,resourceGroup,old_resource_group)

# table_service = make_connection()

# print(ent)


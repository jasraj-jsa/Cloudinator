from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity
from data_ingestion.connection_string import CONNECTION_STRING






# res_id = ',subscriptions,0fee9a15-8774-4097-a3ec-07f63b029db0,resourceGroups,dummy-res-grp,providers,Microsoft.Compute,virtualMachines,testvm1'
# user_id = 'test_1@citrix.com'
# res_name = "testvm1"
# res_type = "Microsoft.Compute/virtualMachines"
# sub_name = "cge-dev-techproject-5317"
# creation_date = None
# last_access_date = None
# recent_user1_ID = None
# recent_user2_ID = None
# metrics = None
# cost_last_month = None
# cost_total = None
# res_status = None
# user_notified = False
# user_last_notified_date = None
# way_notified = None

# entity = {
#     'PartitionKey' : user_id, 
#     'RowKey' : res_id,
#     'ResName' : res_name,
#     'ResType' : res_type,
#     'SubName' : sub_name,
#     'CreationDate' : creation_date,
#     'LastAccessDate' : last_access_date,
#     'RecentUser1ID' : recent_user1_ID,
#     'RecentUser2ID' : recent_user2_ID,
#     'Metrics' : metrics,
#     'CostLastMonth' : cost_last_month,
#     'CostTotal' : cost_total,
#     'ResStatus' : res_status,
#     'UserNotified': user_notified,
#     'UserLastNotifiedDate' : user_last_notified_date,
#     'WayNotified' : way_notified

# }

def make_connection():
    table_service = TableService(endpoint_suffix = "table.cosmos.azure.com", connection_string = CONNECTION_STRING )
    return table_service

# table_service = make_connection(connection_string= CONNECTION_STRING)

def create_table(table_service, table_name):
    table_service.create_table(table_name)
    # print("Table created with Name: " + table_name )


# create_table(table_service, table_name)

def insert_entity(table_name, table_service, entity ):
    table_service.insert_entity(table_name, entity)
    


# insert_entity(table_name, table_service, entity)

def update_entity(table_name, table_service, entity):
    table_service.update_entity(table_name, entity)

# update_entity(table_name, table_service, entity)

def insert_or_replace_entity(table_name, table_service, entity):
    table_service.insert_or_replace_entity(table_name, entity)

# insert_or_replace_entity(table_name, table_service, entity)

def merge_entity(table_name, table_service, entity):
    table_service.merge_entity(table_name, entity)

# merge_entity(table_name, table_service, entity)

def insert_or_merge_entity(table_name, table_service, entity):
    try:
        table_service.insert_or_merge_entity(table_name, entity)
    except:
        print("failed")

    

# insert_or_merge_entity(table_name, table_service, entity)

def get_entity(table_name, table_service, PartitionKey,RowKey, select=None):
    return table_service.get_entity(table_name, PartitionKey, RowKey, select)

def get_entities(table_name, table_service, filter=None, select=None):
    return table_service.query_entities(table_name, filter, select)

def delete_entity(table_name, table_service, PartitionKey,RowKey):
    table_service.delete_entity(table_name, PartitionKey, RowKey)

def delete_table(table_name, table_service):
    table_service.delete_table(table_name)




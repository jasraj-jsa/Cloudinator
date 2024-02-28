# from data_ingestion_module.connection_string import CONNECTION_STRING
# from data_ingestion_module.data_ingestion import make_connection, insert_or_merge_entity


from resource_operation.modules import delete_resource_by_id, move_resources, delete_resource_groups, deallocate_vm, delete_vm, stop_vm
# from resource_operation.helper import convert_slash_to_comma

def delete_resources_main(resourceId, source_resource_group_name, email_id):
    
    ##making connection with table
    # table_service = make_connection(CONNECTION_STRING)
    target_resource_group_id = "/subscriptions/0fee9a15-8774-4097-a3ec-07f63b029db0/resourceGroups/dump_res_grp"
    target_resource_group_name = "dump_res_grp"

    # print(source_resource_group_name)

    deleteable_info=[]
    delete_async_operation = delete_resource_by_id(resourceId)
    
    if delete_async_operation is None:
        move_resources_main(resource_id_list=[resourceId], source_resource_group_name=source_resource_group_name, target_resource_group_id=target_resource_group_id, email_id=email_id,target_resource_group_name=target_resource_group_name )
        rs_info = {'resource_id': resourceId, 'deletable':False, 'new_resource_grp_name':target_resource_group_name}
        deleteable_info.append(rs_info.copy())

    else:
        delete_async_operation.wait()
        rs_info = {'resource_id': resourceId,'deletable':True, 'new_resource_grp_name':''}
        deleteable_info.append(rs_info.copy())
        # res_entity = {
        #     'PartitionKey': email_id,
        #     'RowKey' : convert_slash_to_comma(res_id),
        #     'ResStatus': 'Deleted'
        # }

        # insert_or_merge_entity(table_name, table_service, res_entity)
        # print(delete_async_operation)

    return deleteable_info

def move_resources_main(resource_id_list, source_resource_group_name, target_resource_group_id, email_id, target_resource_group_name):

    ##making connection with table
    # table_service = make_connection(CONNECTION_STRING)   

    move_async_operation = move_resources(resource_id_list, source_resource_group_name, target_resource_group_id)
    
    if move_async_operation is None:
        print('resource moving operation failed')
        return

    move_async_operation.wait()

    # print(move_async_operation)
    # for res_id in resource_id_list:
    #     res_entity = {
    #         'PartitionKey': email_id,
    #         'RowKey' : convert_slash_to_comma(res_id),
    #         'ResStatus' :'Deallocated'
    #     }

    #     insert_or_merge_entity(table_name, table_service, res_entity)

def delete_resource_group_main(group_name, email_id, table_name):
    # res_list = get_resource_list(group_name)

    #making connection with table
    # table_service = make_connection(CONNECTION_STRING) 

    delete_async_operation = delete_resource_groups(group_name)
    delete_async_operation.wait()

    # if delete_async_operation is not False:
    #     for res in res_list:
    #         res_entity = {
    #             'PartitionKey': email_id,
    #             'RowKey' : convert_slash_to_comma(res.id),
    #             'ResStatus': 'Deleted'
    #         }

    #         insert_or_merge_entity(table_name, table_service, res_entity)

def deallocate_vm_main(group_name, vm_name, email_id, table_name, resource_id):
    deallocate_vm(group_name, vm_name)

    #making connection with table
    # table_service = make_connection(CONNECTION_STRING) 

    # res_entity = {
    #             'PartitionKey': email_id,
    #             'RowKey' : convert_slash_to_comma(resource_id),
    #             'ResStatus': 'deallocated'
    #         }

    # insert_or_merge_entity(table_name, table_service, res_entity) 
    

def delete_vm_main(group_name, vm_name, email_id, table_name, resource_id):
    delete_vm(group_name, vm_name)

    #making connection with table
    # table_service = make_connection(CONNECTION_STRING) 

    # res_entity = {
    #             'PartitionKey': email_id,
    #             'RowKey' : convert_slash_to_comma(resource_id),
    #             'ResStatus': 'deleted'
    #         }

    # insert_or_merge_entity(table_name, table_service, res_entity) 

def stop_vm_main(group_name, vm_name, email_id, table_name, resource_id):
    stop_vm(group_name, vm_name)

    #making connection with table
    # table_service = make_connection(CONNECTION_STRING) 

    # res_entity = {
    #             'PartitionKey': email_id,
    #             'RowKey' : convert_slash_to_comma(resource_id),
    #             'ResStatus': 'stopped'
    #         }

    # insert_or_merge_entity(table_name, table_service, res_entity) 
       


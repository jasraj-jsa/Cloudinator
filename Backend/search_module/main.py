import requests
from utils import get_bearer_token
from credentials import CREDENTIALS

# def search_resource_by_owner(client,owner_email,resource_group=None):
#     '''
#          @args:         client : ResourceManagementClient
#                         owner_email: Owner's email id to search 
#                         resource_group: Resource group to search in ,default value is None
#                                         if None search for all resources

#          @returns:      resource_list: list of resources owned by the email id

#          example of resource object:

#          {'additional_properties': {}, 'id': '/subscriptions/0fee9a15-8774-4097-a3ec-07f63b029db0/resourceGroups/dummy-res-grp/providers/Microsoft.Network/virtualNetworks/dummy-res-grp-vnet', 
#          'name': 'dummy-res-grp-vnet', 'type': 'Microsoft.Network/virtualNetworks', 
#          'location': 'centralindia', 'tags': {'Owner': 'test_2@citrix.com'}, 
#          'plan': None, 'properties': None, 'kind': None, 
#          'managed_by': None, 'sku': None, 'identity': None, 'created_time': None, 
#          'changed_time': None, 'provisioning_state': None }

#     '''

#     if resource_group is not None:

#         all_resource_list = client.resources.list_by_resource_group(resource_group)
#     else:
#         all_resource_list=client.resources.list()

    

#     resource_list=[]

#     for rs in list(all_resource_list):
    
#         if rs.tags is not None and (('Owner' in rs.tags and rs.tags['Owner']==owner_email )or ('owner' in rs.tags and rs.tags['owner']==owner_email)):
#             resource_list.append(rs)




#     return resource_list

def get_resource_group(idx):
    pos=idx.find('resourceGroups')

    sub=idx[pos+15:]
    

    hash_pos=sub.find('/')

    return idx[pos +15: pos+hash_pos+15]

def search_resource_by_owner_rest(owner_email,resource_group=None):

    PARAMS = {'Authorization':get_bearer_token(),
    'Host':"management.azure.com"
    }
    ##getting all resources in the subscription

    if resource_group==None:
        URL = f"https://management.azure.com/subscriptions/{CREDENTIALS['subscriptionId']}/resources?api-version=2020-09-01"
    else:
        URL = f"https://management.azure.com/subscriptions/{CREDENTIALS['subscriptionId']}/resourcegroups/{resource_group}/resources?api-version=2020-09-01"
    subscription_name=requests.get(url=f"https://management.azure.com/subscriptions/{CREDENTIALS['subscriptionId']}?api-version=2016-06-01",params=PARAMS,headers=PARAMS).json()['displayName']
    all_resource_list = requests.get(url = URL,params=PARAMS,headers=PARAMS)


    # print(all_resource_list.json())

    all_resource_list=all_resource_list.json()['value']
    
    resource_list=[]

    for rs in list(all_resource_list):
        if 'tags' in rs.keys() and rs['tags'] is not None and (('Owner' in rs['tags'] and rs['tags']['Owner']==owner_email )or ('owner' in rs['tags'] and rs['tags']['owner']==owner_email)):
            rs['owner'] = owner_email
            resgroupid=get_resource_group(rs['id'])
            rs['resourceGroup']=resgroupid
            # print(resgroupid)
            rs['subscriptionName'] = subscription_name
            resource_list.append(rs)




    return resource_list



    



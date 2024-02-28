import adal
from credentials import CREDENTIALS
def get_bearer_token():
    authority_uri = CREDENTIALS['activeDirectoryEndpointUrl'] + "/" + CREDENTIALS['tenantId']
    context = adal.AuthenticationContext(authority_uri)
    token = context.acquire_token_with_client_credentials(
                CREDENTIALS["resourceManagerEndpointUrl"],
                CREDENTIALS['clientId'],
                CREDENTIALS['clientSecret'])
    bearer = "bearer " + token.get("accessToken")
    return bearer

def convert_slash_to_comma(s):
    return s.replace('/',',')

def create_entity(ResourceId,Owner):
    return {
       'RowKey': convert_slash_to_comma(ResourceId),
        'PartitionKey': Owner
    }
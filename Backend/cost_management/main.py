import json
import requests
from credentials import CREDENTIALS
from utils import get_bearer_token


def transform(costData, payloadjson, headers,response):
    result = json.loads(response)
    for record in result["properties"]["rows"]:
        usageRecord = {}
        for index, val in enumerate(record):
            columnName = result["properties"]["columns"][index]
            if columnName["type"] == "number":
                usageRecord[columnName["name"]] = float(val)
            else:
                usageRecord[columnName["name"]] = val

        costData.append(usageRecord)
    nextLink = result["properties"]["nextLink"]
    if nextLink != None:
        nextLinkResponse = requests.post(nextLink, data=payloadjson, headers = headers)
        if nextLinkResponse.status_code == 200:
            transform(costData,payloadjson, headers,nextLinkResponse.text)
        else:
            print("error in fetching next page " + nextLink)
            print("error " + nextLinkResponse.text)

def cost_analysis(ResourceId):
    costmanagementUrl = "https://management.azure.com/subscriptions/" + CREDENTIALS["subscriptionId"] + "/providers/Microsoft.CostManagement/query?api-version=2019-11-01"
    headers = { "Authorization" : get_bearer_token(), "Content-Type": "application/json" }
    payload = {
        "type": "Usage",
        "timeframe": "MonthToDate",
        "dataset": {
        "granularity": "None",
        "aggregation": {
        "totalCost": {
            "name": "PreTaxCostUSD",
            "function": "Sum"
            }
        },
        "grouping": [
            {
            "type": "Dimension",
            "name": "ResourceId"
            }
            # {
            # "type": "Dimension",
            # "name": "ResourceGroup"
            # },
            # {
            # "type": "Dimension",
            # "name": "ResourceType"
            # }
        ],
        "filter": {
            "dimensions":{
                "name": "ResourceId",
                "operator": "In",
                "values": [ResourceId]
            }
        }
        }
    }
    payloadjson = json.dumps(payload)
    costData = []
    response = requests.post(costmanagementUrl, data=payloadjson, headers = headers)
    if response.status_code == 200:
        transform(costData,payloadjson, headers,response.text)            
    else:
        print("error")   
        print("error " + response.text)
    # json_object = json.dumps(costData, indent = 4)
    # with open("sample.json", "w") as outfile:
    #     outfile.write(json_object)
    cost = 0
    if(len(costData)):
        cost = costData[0]["PreTaxCostUSD"]
    return cost







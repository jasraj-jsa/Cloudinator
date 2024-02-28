import requests
from datetime import datetime, timedelta
from utils import get_bearer_token



def metric(resId):
    currentTime = datetime.now().replace(microsecond=0)
    prevmonthTime = (currentTime - timedelta(30)).isoformat()
    h1 = { "Authorization" : get_bearer_token(), "Content-Type": "application/json" }
    url="https://management.azure.com/" + resId + "/providers/Microsoft.Insights/metrics?timespan=" + prevmonthTime + "Z/" + currentTime.isoformat() + "Z&interval=P1D&aggregation=Average&api-version=2018-01-01"
    response = requests.get(url,headers=h1)
    data=response.json()
    #print(data)
    if ("value" in data.keys())==False:
        return False
    avg=0.0
    n=1
    flag = False
    if('value' in data and len(data['value']) and 'timeseries' in data["value"][0] and len(data['value'][0]['timeseries']) and "data" in data['value'][0]['timeseries'][0]):
        total_data = data['value'][0]['timeseries'][0]['data']
        flag = True  
    if(flag):
        for i in total_data:
            if len(i)==2 :
                #print(i)
                avg=avg+i['average']
                n=n+1
    return avg/n
    #return "NO"

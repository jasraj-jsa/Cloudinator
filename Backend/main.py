from flask import Flask, request
from bson import json_util
from modules import searchDB,refreshDB,deallocate_resource,notify_users
import json
app = Flask(__name__)

@app.route("/searchDB",methods = ["GET"])
def search():
    username = request.args.get("username")
    if(not(username) or username == ''):
        return ("",204)
    entities = searchDB(username)
    return (json.dumps(entities,default=json_util.default),200)

@app.route("/refreshDB",methods = ["GET"])
def refresh():
    username = request.args.get("username")
    if(not(username) or username == ''):
        return ("",204)
    refreshDB(username)
    return ({},200)

@app.route("/deallocateResource",methods=["POST"])
def deallocate():
    # print(request)
    body = request.get_json()
    deallocate = deallocate_resource(body["resourceId"],body["resourceGroup"],body["owner"])
    if(deallocate):
        return ({},200)
    return ({},500)

@app.route("/notifyUser",methods = ["POST"])
def notify():
    body = request.get_json()
    user1 = ""
    user2 = ""
    oldrg = ""
    if("recentUser1" in body):
        user1 = body["recentUser1"]
    if("recentUser2" in body):
        user2 = body["recentUser2"]
    if("oldResourceGroup" in body):
        oldrg = body["oldResourceGroup"]
    if((user1 and user1!="") or (user2 and user2!="")):
       notify_users(user1,user2,body["owner"],body["resourceName"],body["resourceType"],body["subscriptionName"],body["resourceStatus"],body["resourceGroup"],oldrg)
    return ({},200)
    

    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    
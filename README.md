# Cloudinator
A platform to identify and manage cloud resources tied to ex-employees, enhancing security and cost-efficiency.

### Problem Statement: A lot of dev cloud resources are left behind after the employee leaves the organization posing security threats, ownership gaps and redundant cost to the team and organization. 

### Solution
- Scan target azure subscription(s) for the resources that are tagged with 'Owner' and value matches with the email address of ex-employee.
- Analyze the Activity Logs  and Network Metrics of the scanned resources.
- Stop/Deallocate the resources immediately.
- Notify the user from activity log who interacted with the resource recently about deallocating the instance and time period after which resource will be permanently deleted.
- Wait for the notified time period and then permanently delete these dummy resources.


### Software Requirements
1) NodeJS(npm)
2) Python(pip)

-> Frontend
```
cd Frontend
npm install
npm start
```

-> Backend
```
cd Backend
pip install -r requirements.txt
python main.py
```

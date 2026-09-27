import json, os

FILE = "user_data.json"

def save_user_plan(user_id, details, plan):
    data = {}
    if os.path.exists(FILE):
        with open(FILE,'r') as f:
            data = json.load(f)
    if user_id not in data:
        data[user_id] = []
    data[user_id].append({"details": details, "plan": plan})
    with open(FILE,'w') as f:
        json.dump(data, f, indent=4)

def get_user_plans(user_id):
    if not os.path.exists(FILE):
        return []
    with open(FILE,'r') as f:
        return json.load(f).get(user_id, [])

def get_all_users():
    if not os.path.exists(FILE):
        return {}
    with open(FILE,'r') as f:
        return json.load(f)
import json

file = open("payments.json")
employees = json.load(file)["employees"]
emp = []
for i in employees:
    emp.append({i["name"]: i["job_title"]})

print(emp)

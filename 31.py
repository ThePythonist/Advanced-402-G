import json

file = open("payments.json")
employees = json.load(file)["employees"]
emp = []
for i in employees:
    print(i["name"],end=" : ")
    all = sum(i["monthly_payment"].values())
    print(all/12)


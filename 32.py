import json
from colorama import Fore

file = open("payments.json")
employees = json.load(file)["employees"]
emp = {}
for i in employees:
    all = sum(i["monthly_payment"].values())
    emp.update({i["name"]: all / 12})

# for i in emp.items():
#     print(i)
#
# print(Fore.RED + "Most Paid Employee :", max(emp.items()))

mostpaid = max(emp.items())

for i in emp.items():
    if i[1] == mostpaid[1]:
        print(Fore.RED + "Most Paid Employee :", i)
    else:
        print(Fore.WHITE + "", i)

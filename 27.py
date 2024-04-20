import json

file = open('states.json')
data = json.load(file)

# print(len(data["states"]))

for i in data["states"]:
    print(i)

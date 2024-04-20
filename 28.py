import json

file = open('states.json')
data = json.load(file)

state_names = []

for i in data["states"]:
    state_names.append((i["name"]))

new_file = open("state_names.json", "w")
json.dump(state_names, new_file, indent=2)

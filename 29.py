import json

file = open("states.json")
file = json.load(file)

selected_states = []

for i in file["states"]:
    if i["name"].lower() in ["new york", "florida", "alaska"]:
        selected_states.append(i)

file2 = open("selected_states.json", "w")
json.dump(selected_states, file2, indent=4)

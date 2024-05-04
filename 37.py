import xmltodict

xml_data = open("flights.xml").read()
data_dict = xmltodict.parse(xml_data)

root = data_dict['flights']
flights = root['flight']

william_thompson_flights = []

for i in flights:
    for j in i["passengers"]["passenger"]:
        if j["name"] == "William Thompson":
            william_thompson_flights.append(i)

print(william_thompson_flights)

# ---------------------------------------------------------------------

wrapped_data = {'flights': {'flight': william_thompson_flights}}

xml_string = xmltodict.unparse(wrapped_data, pretty=True)
open("william_flights.xml", "w").write(xml_string)

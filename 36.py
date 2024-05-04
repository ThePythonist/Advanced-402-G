import xmltodict

xml_file = open("flights.xml").read()
data = xmltodict.parse(xml_file)
root = data["flights"]
flights = root["flight"]

for i in flights:
    if i["destination"].lower() == "paris":
        print(i)

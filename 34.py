import xmltodict

xml_data = open("payments.xml").read()
data = xmltodict.parse(xml_data)

root = data["employees"]
employees = root["employee"]

under_30 = []

for i in employees:
    if int(i["age"]) < 30:
        under_30.append(i)

for i in under_30:
    print(i)

students = [
    {"name": "mohammadreza", "job": "backend-dev", "age": 14},
    {"name": "eghbal", "job": "backend-dev", "age": 17},
    {"name": "amirhossein", "job": "bi kar", "age": 6},
    {"name": "narges", "job": "frontend-dev", "age": 20},
]

html = """
<!DOCTYPE html>
<html>
<head>
    <style>
        #customers {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

#customers td, #customers th {
  border: 1px solid #ddd;
  padding: 8px;
}

#customers tr:nth-child(even){background-color: #f2f2f2;}

#customers tr:hover {background-color: #ddd;}

#customers th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #04AA6D;
  color: white;
}

    </style>
</head>
<body>

<h1>Students Table</h1>

<table id="customers">
    <tr>
        <th>Name</th>
        <th>Job</th>
        <th>Age</th>
    </tr>
"""
for i in students:
    html += f"""
        <tr>
            <td>{i['name']}</td>
            <td>{i['job']}</td>
            <td>{i['age']}</td>
        </tr>
    """

html += """
</table>
</body>
</html>
"""

open("table.html", "w").write(html)

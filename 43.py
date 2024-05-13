header = input("Enter any header : ")
par = input("Enter any paragraph : ")

output = f"""
<h1>{header}</h1>
<p>{par}</p>
"""

open("index.html","w").write(output)
print("Done")

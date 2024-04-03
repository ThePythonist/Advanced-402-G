import sqlite3

con = sqlite3.connect("records.db")
cur = con.cursor()

# cur.execute("CREATE TABLE PHONES (brand,model,price);")
# cur.execute("INSERT INTO PHONES VALUES ('samsung','a52','650');")
# cur.execute("INSERT INTO PHONES VALUES ('xiaomi','note10','500');")

cur.execute("SELECT * FROM PHONES;")
records = cur.fetchall()

for i in records:
    print(i)


con.commit()
con.close()
print("Done")

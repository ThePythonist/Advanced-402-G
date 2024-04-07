import sqlite3

con = sqlite3.connect("info.db")
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS customers (name,city,phone);")

# cur.execute("INSERT INTO customers VALUES ('arian','tabriz','09305541010');")
# cur.execute("INSERT INTO customers VALUES ('ali','tabriz','09306641123');")
# cur.execute("INSERT INTO customers VALUES ('kiana','tehran','09125005030');")

con.commit()
con.close()
print("Done")

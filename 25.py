import sqlite3

con = sqlite3.connect('info.db')
cur = con.cursor()

cur.execute("SELECT * FROM employees;")
records = cur.fetchall()
users = [i[1:] for i in records]

new_record = {"name": "Bahar", "code": 40215, "job": "Civil Engineer"}
new_record = tuple(new_record.values())


# for i in users :
#     print(i)

def save(record):
    command = f"INSERT INTO employees(name,code,job) VALUES {(record[0], record[1], record[2])};"
    # print(command)
    cur.execute(command)


if new_record in users:
    print("User already exists in db")
else:
    save(new_record)
    print("User added to database")


cur.execute("SELECT * FROM employees;")
records = cur.fetchall()


for i in records:
    print(i)

print(len(records), "Users exist in db")

con.commit()
con.close()

import sqlite3

con = sqlite3.connect("info.db")
cur = con.cursor()

stds = [
    {"name": "farzad", "field": "civil engineering", "grade": "16"},
    {"name": "helia", "field": "computer engineering", "grade": "19"},
    {"name": "hamed", "field": "architecture", "grade": "13"},
    {"name": "reza", "field": "law", "grade": "18"},
]


def insert(item):
    command1 = "CREATE TABLE IF NOT EXISTS students(name,field,grade);"
    cur.execute(command1)

    command2 = f"INSERT INTO students VALUES {(item['name'], item['field'], item['grade'])};"
    cur.execute(command2)
    con.commit()


def select(table):
    command = f"SELECT * FROM {table};"
    cur.execute(command)
    records = cur.fetchall()
    for i in records:
        if float(i[-1]) >= 17:
            print(i)

for i in stds:
    insert(i)


con.commit()
con.close()
print("Done")

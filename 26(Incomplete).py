import sqlite3


def create(table):
    con = sqlite3.connect("info.db")
    cur = con.cursor()
    columns = tuple(input("Table columns (seperated by comma) : ").split(","))

    query = f"CREATE TABLE IF NOT EXISTS {table} {columns};"
    cur.execute(query)
    # print(query)

    con.commit()
    con.close()
    print("----------------- Table Created -----------------")
    print()
    main()

def insert():
    print("inserted")
    main()


def select():
    print("result :")
    main()

def main():
    operation = input("""
1 : Create table
2 : Insert data into a table
3 : Select data from a table
: """)

    if operation == "1":
        table_name = input("Table name : ")
        create(table_name)
    elif operation == "2":
        insert()
    elif operation == "3":
        select()
    else:
        print("Invalid operation. Try again")
        main()

main()

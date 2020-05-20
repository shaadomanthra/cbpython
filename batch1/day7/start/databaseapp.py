import sqlite3 as lite

def connect(database_name):
    try:
        conn = lite.connect(database_name)
        return conn
    except lite.Error as e:
        print("Some error - " + e)

def execute(conn,query):
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except lite.Error as e:
        print("Some error - " + e)

# to print the version
conn =connect("sample.db")
query1 = "select sqlite_version()"
print(execute(conn,query1))

query2 = "SELECT age FROM student"
print(execute(conn,query2))

query3 = "SELECT * FROM student where name='Sample'"
print(execute(conn,query3))

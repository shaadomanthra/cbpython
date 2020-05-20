import db
# to print the version
conn =db.connect("sample.db")
query1 = "select sqlite_version()"
print(db.execute(conn,query1))

query2 = "SELECT age FROM student"
print(db.execute(conn,query2))

query3 = "SELECT * FROM student where name='Sample'"
print(db.execute(conn,query3))

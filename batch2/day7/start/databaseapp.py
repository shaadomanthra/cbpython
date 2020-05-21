import db

conn = db.connect("test.db")
result = db.execute(conn,"SELECT * from student")
print(result)

result = db.execute(conn,"SELECT id from student")
print(result)

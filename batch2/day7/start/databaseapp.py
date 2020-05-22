import db

conn = db.connect("test.db")
# result = db.fetchall(conn,"SELECT * from student")
# print(result)
#
# result = db.fetchone(conn,"SELECT name from student WHERE id=1")
# print(result)

# query1= "INSERT into student (name,age) VALUES ('Mahesh babu',40)"
# db.insert(conn,query1)

# query2 = "UPDATE student SET age=35 WHERE id=7"
# db.update(conn,query2)

# query3 = "DELETE FROM student WHERE id =6"
# db.delete(conn,query3)

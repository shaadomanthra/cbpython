import db
# to print the version
conn =db.connect("sample.db")
# query1 = "select sqlite_version()"
# print(db.execute(conn,query1))

# query2 = "SELECT * FROM student"
# print(db.fetchall(conn,query2))



# query4 =  "INSERT INTO student (name,rollnumber,age) VALUES ('Naveen',1006,45)"
# db.insert(conn,query4)
query2 = "SELECT * FROM student where id = 5"
print(db.fetchone(conn,query2))

# query5 ="UPDATE  student SET age=50 WHERE id=5"
# db.update(conn,query5)

# query3 = "SELECT * FROM student where id = 5"
# print(db.fetchone(conn,query3))

# query5 = "DELETE FROM student WHERE id =5"
# db.delete(conn,query5)

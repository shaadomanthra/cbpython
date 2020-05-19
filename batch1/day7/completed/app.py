import db

# create conncetion object
conn = db.connect('test.db')
db.version(conn)

# insert statement
query="INSERT INTO student (name,rollnumber,age) VALUES ('Suresh',1004,29)"
db.insert(conn,query)

# select multiple records
query = "SELECT * from student"
result = db.fetchall(conn,query)
for r in result:
    print(r)

# select one record
query = "SELECT * from student where id = 1"
result = db.fetchone(conn,query)
print(result)

# update a record
query = "UPDATE student SET age=30 WHERE id=2"
db.update(conn,query)

# delete a record
query = "DELETE from student WHERE id = 3"
db.delete(conn,query)

# close connection
db.close(conn)

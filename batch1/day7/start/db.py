import sqlite3 as lite

# connect to the database
def connect(database_name):
    connection = lite.connect(database_name)
    return connection

# print sqlite version
def version(connection):
    cursor = connection.cursor()
    query = "select sqlite_version()"
    cursor.execute(query)
    record = cursor.fetchall()
    print(record)
# insert one record into table

# fetch all records from table

# fetch one record from table

# update one record in the table

# delete one record from table

# close the connection

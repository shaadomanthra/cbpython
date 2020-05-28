import sqlite3 as lite

class HelloDB:

    def __init__(self,database_name):
        self.conn = lite.connect(database_name)

    def insert(query):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            self.conn.commit()  # saves the data onto the disk
        except lite.Error as e:
            print(e)
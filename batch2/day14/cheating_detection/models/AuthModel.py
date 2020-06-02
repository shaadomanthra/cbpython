from lib.db import *

class AuthModel:

    def __init__(self):
        self.conn = connect("app.db")

    def getUser(self,username,password):
        query = f"SELECT * FROM users WHERE username='{username}' and password='{password}' "
        result = fetchone(self.conn,query)
        return result

    def createUser(self,name,phone,email,username,password,role):
        query = f"INSERT INTO users (name,phone,email,username,password,role)" \
                f" VALUES ('{name}',{phone},'{email}','{username}','{password}','{role}')"

        result = insert(self.conn,query)
        return result

if __name__ == '__main__':
    am = AuthModel()


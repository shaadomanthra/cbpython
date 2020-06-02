from db import *

class AuthModel:

    def __init__(self):
        self.conn = connect("app.db")

    def getUser(self,username,password):
        query = f"SELECT * FROM users WHERE username='{username}' and password='{password}' "
        result = fetchone(self.conn,query)
        print(result)

    def createUser(self,name,phone,email,username,password,role):
        query = f"INSERT INTO users (name,phone,email,username,password,role)" \
                f" VALUES ('{name}',{phone},'{email}','{username}','{password}','{role}')"
        insert(self.conn,query)
        print("The record is inserted")

am = AuthModel()
am.createUser('krishna',8888888888,'krishna@gmail.com','krishna','krishna123','student')


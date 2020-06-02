
from db import *

class AuthModel:

    def __init__(self):
            self.conn = connect('app.db')

    def getUser(self,username,password):
        query  = f"SELECT * FROM users WHERE username='{username}' and password ='{password}' "
        result =  fetchone(self.conn, query)
        print(result)


am  = AuthModel()
am.getUser('teja','teja123')

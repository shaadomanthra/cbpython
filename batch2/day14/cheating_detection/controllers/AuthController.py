from models.AuthModel import AuthModel

class AuthController:

    def login(self,username,password):
        am = AuthModel()
        result = am.getUser(username,password)
        if result:
            message = f'User found {result[1]}'
        else:
            message = f'User not found'

        return message

    def register(self,name,phone,email,username,password,role):
        am = AuthModel()
        result = am.createUser(name,phone,email,username,password,role)
        if result:
            print("Successfully inserted")
        else:
            print("Some problem")
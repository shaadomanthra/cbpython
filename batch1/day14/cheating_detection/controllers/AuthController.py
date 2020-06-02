from models.AuthModel import AuthModel

class AuthController:

    def login(self,username,password):

        if len(username) == 0:
            print("Username cannot be empty")

        if len(password) == 0:
            print("password cannot be empty")

        am = AuthModel()
        result =  am.getUser(username,password)

        if result:
            message = f'Hello {result[1]}'
            return message
        else:
            message = 'User not found'
            return message




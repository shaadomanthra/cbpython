from models.AuthModel import AuthModel

class AuthController:

    def login(self,username,password):

        if len(username) == 0 :
            message = "Username cannot be empty"
            return message

        if len(password) == 0:
            message = "Password cannot be empty"
            return message

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
            message = 'Successfully created the user. You can login now'
            return message
        else:
            print("Some problem")
            message = 'There is some issue in storing the data, kindly retry'
            return message
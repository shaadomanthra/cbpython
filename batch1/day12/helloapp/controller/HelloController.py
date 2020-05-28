from model.HelloModel import HelloDB
class Hello:

    def __init__(self,view):
        self.hellodb = HelloDB('hellodb')
        self.view = view

    def hello_basic(self):
        self.view.l1.config(text="I have changed it")
        query = "INSERT INTO entries (message) VALUES('hello basic')"
        self.hellodb.insert(query)
        print("Hello")

    def hello_name(self):
        query = "INSERT INTO entries (message) VALUES('hello name')"
        self.hellodb.insert(query)
        print("Hello Teja")

    def hello_in_french(self):
        query = "INSERT INTO entries (message) VALUES('hello in french')"
        self.hellodb.insert(query)
        print("Bonjour")

from model.HelloModel import HelloDB
class Hello:

    def __init__(self,view):
        self.hellodb = HelloDB('hellodb')
        self.view = view

    def hello_basic(self):
        self.view.l1.config(text="Hello Basic is Clicked")
        query = "INSERT INTO entries (message) VALUES('hello basic')"
        self.hellodb.insert(query)
        print("Hello")

    def hello_name(self):
        self.view.l1.config(text="Hello Name is Clicked")
        query = "INSERT INTO entries (message) VALUES('hello name')"
        self.hellodb.insert(query)
        print("Hello Teja")

    def hello_in_french(self):
        self.view.l1.config(text="Hello in french is Clicked")
        query = "INSERT INTO entries (message) VALUES('hello in french')"
        self.hellodb.insert(query)
        print("Bonjour")

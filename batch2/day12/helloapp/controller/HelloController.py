from model.HelloModel import HelloDB
class Hello:

    def __init__(self,view):
        self.hellodb = HelloDB('app.db')
        self.view = view

    def hello_basic(self):
        self.view.l1.config(text="Hello Basic")
        query = "INSERT INTO entries (message) VALUES ('hello basic')"
        self.hellodb.insert(query)


    def hello_name(self):
        self.view.l1.config(text="Hello Name")
        query = "INSERT INTO entries (message) VALUES ('hello name')"
        self.hellodb.insert(query)

    def hello_in_french(self):
        self.view.l1.config(text="Hello in French")
        query = "INSERT INTO entries (message) VALUES ('hello in french')"
        self.hellodb.insert(query)


class Hello:

    def __init__(self,view):
        self.view = view

    def hello_basic(self):
        self.view.l1.config(text="Hello")


    def hello_name(self):
        print("Hello Teja")

    def hello_in_french(self):
        print("Bonjour")

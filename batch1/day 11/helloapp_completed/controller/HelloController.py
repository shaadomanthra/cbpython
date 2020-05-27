
class Hello:

    def __init__(self,master):
        self.view = master

    def hello_basic(self):
        self.view.label.config(text="Hello")

    def hello_name(self):
        self.view.label.config(text="Hello Teja")

    def hello_in_french(self):
        self.view.label.config(text="Bonjour")

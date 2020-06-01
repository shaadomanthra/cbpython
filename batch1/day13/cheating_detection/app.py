
from views.AuthView import AuthView

class MyApp:

    def run(self):
        av = AuthView()
        av.load()

    def printSomething(self):
        print("This is My App print function")


app = MyApp()
app.run()
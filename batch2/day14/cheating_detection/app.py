
from views.AuthView import AuthView

class MyApp:

    def __init__(self):
        av = AuthView()
        av.load()

app = MyApp()

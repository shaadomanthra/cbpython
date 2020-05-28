from controller.HelloController import Hello
from view.LayoutView import Layout

class MyApp():

    def execute(self):
        view = Layout()


app = MyApp()
app.execute()

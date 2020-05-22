from controller.HelloController import Hello
from controller.StringController import StringApp

class MyApp:

    def run(self):
        h = Hello()
        h.hello_basic()

    def stringRun(self,str):
        s = StringApp()
        s.reverse(str)

app = MyApp()
app.run()
app.stringRun("Krishna Teja")

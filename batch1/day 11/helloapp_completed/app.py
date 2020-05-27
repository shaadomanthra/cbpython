
from view.LayoutView import ViewLayout

class MyApp():

    def execute(self):
        view = ViewLayout();
        view.master.mainloop()

app = MyApp()
app.execute()

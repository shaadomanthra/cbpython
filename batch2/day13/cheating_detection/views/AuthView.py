from tkinter import *
from tkinter import ttk

class AuthView:

    def __init__(self):
        window = Tk()
        window.title("My Application")

        tab_control = ttk.Notebook(window)

        login_tab = ttk.Frame(tab_control)
        register_tab =  ttk.Frame(tab_control)

        tab_control.add(login_tab, text="Login")
        tab_control.add(register_tab, text = "Register")

        self.login(login_tab)
        self.register(register_tab)

        tab_control.grid()

        window.mainloop()

    def login(self,login_tab):

        window = login_tab

        ul = Label(window, text="Username")
        ul.grid(row=0,column=0)

        ue = Entry(window, width=10)
        ue.grid(row=0,column=1)

        pl = Label(window, text="Password")
        pl.grid(row=1,column=0)

        pe = Entry(window, show='*',width=10)
        pe.grid(row=1,column=1)

        b = Button(window, text="Login")
        b.grid(row=2,column=1)



    def register(self,register_tab):

        window = register_tab

        # Create name label and entry
        nl = Label(window, text="Name")
        nl.grid(row=0, column=0)

        ne = Entry(window, width=10)
        ne.grid(row=0, column=1)

        #  create email label and entry
        el = Label(window, text="Email")
        el.grid(row=1, column=0)

        ee = Entry(window, width=10)
        ee.grid(row=1, column=1)

        #  create phone label and entry
        phl = Label(window, text="Phone")
        phl.grid(row=2, column=0)

        phe = Entry(window, width=10)
        phe.grid(row=2, column=1)

        # Create username label and entry
        ul = Label(window, text="Username")
        ul.grid(row=3, column=0)

        ue = Entry(window, width=10)
        ue.grid(row=3, column=1)

        # Create password label and entry
        pl = Label(window, text="Password")
        pl.grid(row=4, column=0)

        pe = Entry(window, show='*', width=10)
        pe.grid(row=4, column=1)

        #  create a button register
        b = Button(window, text="Register")
        b.grid(row=5, column=1)



av = AuthView()



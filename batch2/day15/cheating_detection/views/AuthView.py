from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from controllers.AuthController import AuthController

class AuthView:

    def load(self):
        window = Tk()
        window.title("My Application")

        tab_control = ttk.Notebook(window)

        login_tab = Frame(tab_control,bg="white",padx=10,pady=10)
        register_tab =  Frame(tab_control,bg="white",padx=10,pady=10)

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

        b = Button(window, text="Login",command=lambda: self.loginControl(ue.get(),pe.get()))
        b.grid(row=2,column=1)

    def loginControl(self,username,password):
        ac = AuthController()
        print('Username',username)
        print('Password',password)
        message = ac.login(username,password)

        if message:
            messagebox.showinfo('Alert',message)

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
        b = Button(window, text="Register", command=lambda: self.registerControl(ne.get(),phe.get(),ee.get(),
                                                                                 ue.get(),pe.get()))
        b.grid(row=5, column=1)

    def registerControl(self,name,phone,email,username,password):

        ac = AuthController()
        message = ac.register(name,phone,email,username,password,'student')

        if message:
            messagebox.showinfo('Alert',message)


av = AuthView()



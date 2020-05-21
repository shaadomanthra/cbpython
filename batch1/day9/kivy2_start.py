import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class Myappli(App):

    def build(self):
        return Label(text="Welcome to Kivy")

Myappli().run()

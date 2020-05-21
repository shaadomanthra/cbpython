import kivy
from kivy.app import App
from kivy.uix.label import Label

class Myappli(App):

    def build(self):
        return Label(text="Welcome to Kivy")

Myappli().run()

# main.py
# Modified from https://kivy.org/doc/stable/guide/basic.html
import kivy
kivy.require('1.11.1')  # Set to your Kivy version
# print(kivy.__version__)
from kivy.app import App
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        return Button(text='This is a button.')


MyApp().run()
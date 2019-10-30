import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
kivy.require('1.11.1')

class MyApp(App):
    def build(self):
        grid = GridLayout(cols=2,rows=4)
        grid.add_widget(Button(text='Off'))
        arctic = Button(text='Artic Scene', background_color=(0,220,220,1))
        arctic.on_press = lambda: print('trigger arctic')

        grid.add_widget(arctic)
        grid.add_widget(Button(text='Button 3'))
        grid.add_widget(Button(text='Button 4'))
        
        return grid


if __name__ == '__main__':
     MyApp().run()

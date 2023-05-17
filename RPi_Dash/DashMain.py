import kivy
from kivy.app import App
from kivy.uix.label import Label

kivy.require('2.1.0') # replace with your current kivy version !

class MyApp(App):

    def build(self):
        return Label(text='Hello world')


if __name__ == '__main__':
    MyApp().run()
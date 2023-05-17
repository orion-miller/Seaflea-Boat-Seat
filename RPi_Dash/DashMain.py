import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.config import Config

kivy.require('2.1.0') # replace with your current kivy version !

Config.set('graphics', 'width', '320')
Config.set('graphics', 'height', '240')

class MyApp(App):

    def build(self):
        self.title = "Dash"
        return Label(text='BATTERY: 100%')
        
if __name__ == '__main__':
    MyApp().run()
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.config import Config
from kivy.core.window import Window

kivy.require('2.1.0') # replace with your current kivy version !

#Set window resolution and turn off resizing
Window.size = (320, 240)
Config.set('graphics', 'resizable', False) 
Config.write()       
class MyApp(App):

    def build(self):
        #Set properties for window
        self.title = "Dash"
        self.icon = "Images//OM_Logo_32_32.ico"
        self.root = BoxLayout()

        #Set widgets
        self.root.orientation = 'vertical'
        self.root.add_widget(Label(text='   TIME: 11:03 AM', font_size='20sp', halign='left'))        
        self.root.add_widget(Label(text='  SPEED: 28 MPH', font_size='20sp'))
        self.root.add_widget(Label(text='    RPM: 2550', font_size='20sp'))
        self.root.add_widget(Label(text='HEADING: NNE', font_size='20sp'))
        self.root.add_widget(Label(text=' LIGHTS: ON', font_size='20sp'))

        return self.root
        
if __name__ == '__main__':
    MyApp().run()
import time

import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.config import Config
from kivy.core.window import Window
from kivy.clock import Clock

kivy.require('2.1.0') # replace with your current kivy version !

#Set window resolution and turn off resizing
Window.size = (320, 240)
Config.set('graphics', 'resizable', False) 
Config.write()   

class myclock(Label):
    def update(self, *args):
        #Updates the clock value each second
 
          # get the current local time
        self.text = "        TIME: " + time.asctime().split(' ')[3]
        self.font_size = '20sp'
        self.font_name = 'RobotoMono-Regular'
        self.halign = 'left'

class MyApp(App):

    def build(self):
        #Set properties for window
        self.title = "Dash"
        self.icon = "Images//OM_Logo_32_32.ico"
        self.root = BoxLayout()

        #Set widgets
        self.root.orientation = 'vertical'

        self.label_time = myclock() # calling clock class for time        
        self.label_speed = Label(text='       SPEED: 28 MPH', font_size='20sp', font_name='RobotoMono-Regular', halign='left')
        self.label_rpm = Label(text='         RPM: 2550', font_size='20sp', font_name='RobotoMono-Regular', halign='left')
        self.label_heading = Label(text='     HEADING: NNE', font_size='20sp', font_name='RobotoMono-Regular', halign='left')
        self.label_lights = Label(text='      LIGHTS: ON', font_size='20sp', font_name='RobotoMono-Regular', halign='left')        

        # updates time with the interval of 1 sec
        Clock.schedule_interval(self.label_time.update, 1)

        self.label_time.bind(size=self.label_time.setter('text_size')) 
        self.label_speed.bind(size=self.label_speed.setter('text_size')) 
        self.label_rpm.bind(size=self.label_rpm.setter('text_size')) 
        self.label_heading.bind(size=self.label_heading.setter('text_size'))         
        self.label_lights.bind(size=self.label_lights.setter('text_size')) 
                 
        self.root.add_widget(self.label_time)      
        self.root.add_widget(self.label_speed) 
        self.root.add_widget(self.label_rpm) 
        self.root.add_widget(self.label_heading) 
        self.root.add_widget(self.label_lights)       

        return self.root
        
if __name__ == '__main__':
    MyApp().run()
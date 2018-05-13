import kivy #import module
kivy.require('1.10.0') #based on your Kivy version

#import modules from kivy
from kivy.app import App
from kivy.uix.button import Label

#inherit kivy apps class
class HelloKivy(App):

    def build(self):
        return Label(text="Hello Kivy")

helloKivy = HelloKivy()

helloKivy.run()

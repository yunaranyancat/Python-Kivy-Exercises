import kivy

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.popup import Popup

class CustomPopup(Popup):
    pass

class SampBoxLayout(BoxLayout):

    checkbox_is_active = ObjectProperty(False)

    def checkbox_18_clicked(self, instance, value):
        if value is True:
            print("Checkbox Checked")
        else:
            print("Checkbox is Unchecked")

    blue = ObjectProperty(True)
    red = ObjectProperty(False)
    green = ObjectProperty(False)

    def switch_on(self, instance, value):
        if value is True:
            print("Switched On")
        else:
            print("Switched Off")

class SampleApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return SampBoxLayout()

sample_app = SampleApp()
sample_app.run()

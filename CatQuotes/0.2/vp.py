#!python

from kivy.app import App
from kivy.factory import Factory
from viewport import Viewport

class ViewportApp(App):
    def build(self):
        self.root = Viewport(size=(1080,1920))
        self.root.add_widget(Factory.Button(text="ViewportApp"))
        return self.root

if __name__ == "__main__":
    ViewportApp().run()

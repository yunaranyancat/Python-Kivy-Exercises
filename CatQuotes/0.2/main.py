# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from functools import partial
from kivy.uix.button import Label


import sys

Builder.load_file('catquotes.kv')

data_init = ['“Honestly, being lonely is really addicting, and that addiction might lead to something really bad and painful, like me.. now I’m stuck at the window waiting someone to help me to get out from this stupid situation.. ” - Lonely cat '\
            ,'“ You don’t need to find too far away the cat you wanna be with, sometimes you just need to look down, literally…. just to see there’s someone already waiting for you.. - High standard cat'\
            ,'“ Her eyes were so shiny.. Her nose was so geometrically perfect.. Is this an angel?.. Am I dead?.. Am I in heaven?...  Wait a second… AM I REALLY DEAD?!!” - Dead cat'\
            ,'“ The best morning… Is when you wake up, just to see there’s someone lying besides you, with the face saying “wake up and make me a breakfast, I’m hungry..” ” - Chef cat'\
            ,'“ How I wish you were here, but I can’t be selfish.. I know you’re waiting for me at the heaven’s gate. Let’s wait together… I do miss you though..” - Waiting cat'\
            ,'“ I know we are different.. but can’t we go through it together... please???” - Confused cat']



class MenuUI(Widget):
    pass

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        self.menu = MenuUI()
        self.add_widget(self.menu)

class LonelyCatScreen(Screen):

    def __init__(self, **kwargs):
         super(LonelyCatScreen, self).__init__(**kwargs)
         self.requiredtext = data_init[0]
         self.labelObject = None

    def showtext(self):
        temp_list = []

        for child in self.children:
            for smaller_child in child.children:
                for smaller_smaller_child in smaller_child.children:
                    temp_list.append(smaller_smaller_child)


        self.labelObject = temp_list[0]
        self.labelObject.text = self.requiredtext


screen_manager = ScreenManager()

screen_manager.add_widget(MenuScreen(name="menu"))
screen_manager.add_widget(LonelyCatScreen(name="CAT_lonely"))


class CatQuotesApp(App):

    def build(self):
        return screen_manager

if __name__ == "__main__":
    cQ_app = CatQuotesApp()
    cQ_app.run()

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder


class HomeScreen(Screen):

    # kv file loader
    Builder.load_file("styles/home_screen.kv")

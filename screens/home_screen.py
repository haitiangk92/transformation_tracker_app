from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from nav_screens.dashboard import Dashboard
from nav_screens.history import History
from nav_screens.stats import Stats
from nav_screens.settings import Settings


class HomeScreen(Screen):

    # kv file loader
    Builder.load_file("styles/home_screen.kv")

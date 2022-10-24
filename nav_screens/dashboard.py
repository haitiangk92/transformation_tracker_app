from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder


class NavDashboard(Widget):

    # kv file loader
    Builder.load_file("styles/dashboard.kv")

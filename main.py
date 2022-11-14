# Screens
from screens.create_account_screen import CreateAccountScreen
from screens.login_screen import LoginScreen
from screens.home_screen import HomeScreen

# Kivy Modules
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.core.window import Window

APP_WIDTH = 500
APP_HEIGHT = 900


class WindowManager(ScreenManager):
    pass


class TransformationTrackerApp(MDApp):
    def build(self):
        return Builder.load_file("styles/main.kv")

    # def on_start(self):
        # Window.size = (APP_WIDTH, APP_HEIGHT)


if __name__ == "__main__":
    TransformationTrackerApp().run()

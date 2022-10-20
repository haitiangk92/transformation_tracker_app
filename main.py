from screens.create_account_screen import CreateAccountScreen
from screens.login_screen import LoginScreen
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder


class WindowManager(ScreenManager):
    pass


class TransformationTrackerApp(MDApp):
    def build(self):
        return Builder.load_file("styles/main.kv")


if __name__ == "__main__":
    TransformationTrackerApp().run()

from kivymd.app import MDApp

from screens.welcome_screen import WelcomeScreen


class TransformationTrackerApp(MDApp):
    def build(self):
        return WelcomeScreen()


if __name__ == "__main__":
    TransformationTrackerApp().run()

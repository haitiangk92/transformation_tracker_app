from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder


class WelcomeScreen(Widget):

    email = ObjectProperty(None)
    password = ObjectProperty(None)

    kv = Builder.load_file("styles/welcome_screen.kv")

    def btn_clicked(self):
        print(f"Email: {self.email.text}\nPassword: {self.password.text}\n")
        self.email.text = ""
        self.password.text = ""

    def create_account(self):
        print("Create Account")
        self.email.text = ""
        self.password.text = ""

    def forgot_password(self):
        print("Forgot Password")
        self.email.text = ""
        self.password.text = ""

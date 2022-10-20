from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.lang import Builder


class LoginScreen(Screen):

    # kv file loader
    Builder.load_file("styles/login_screen.kv")

    # kv file ids
    email = ObjectProperty(None)
    password = ObjectProperty(None)

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

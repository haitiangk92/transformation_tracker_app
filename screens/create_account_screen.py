from kivymd.uix.widget import MDWidget
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.lang import Builder


class CreateAccountScreen(Screen):

    # kv file loader
    Builder.load_file("styles/create_account_screen.kv")

    # kv file ids
    email = ObjectProperty(None)
    password1 = ObjectProperty(None)
    password2 = ObjectProperty(None)
    first_name = ObjectProperty(None)
    last_name = ObjectProperty(None)

    def check_passwords():
        print("Checking Passwords")

    def btn_clicked(self):
        kv_ids = [self.email, self.password1,
                  self.password2, self.first_name, self.last_name]

        screen = "Welcome" if len(
            self.password1.text) > 3 and self.password2.text == self.password1.text else "CreateAccount"

        for id in kv_ids:
            print(id.text)
            id.text = ""

        return screen

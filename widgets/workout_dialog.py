from kivymd.uix.list import OneLineAvatarIconListItem, IRightBodyTouch
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton, MDIconButton
from kivymd.uix.label import MDLabel


class WorkoutDialogListItem(OneLineAvatarIconListItem):
    """Workout Dialog List Item"""

    def __init__(self, *args, **kwargs):
        super(WorkoutDialogListItem, self).__init__(*args, **kwargs)


class WorkoutDialogLayout(MDBoxLayout):
    orientation = "vertical"
    adaptive_height = True
    spacing = 10

    def __init__(self, *args, workouts=None, width=None, widgets=[], **kwargs):
        super(WorkoutDialogLayout, self).__init__(*args, **kwargs)

        self.size_hint_x = None
        self.width = width

        if workouts:
            for workout in workouts:
                self.add_widget(workout)

        for widget in widgets:
            self.add_widget(widget)

        self.add_widget(
            MDRaisedButton(
                text="+",
                size_hint_x=None,
                width=self.width,
                on_release=self.add_rep
            )
        )

    def add_rep(self, *args):
        print("Adding Rep")

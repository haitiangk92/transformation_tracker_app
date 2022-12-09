from kivymd.uix.list import OneLineAvatarIconListItem
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.scrollview import MDScrollView

import random


class WorkoutDialogListItem(OneLineAvatarIconListItem):
    """Workout Dialog List Item"""

    def __init__(self, *args, **kwargs):
        super(WorkoutDialogListItem, self).__init__(*args, **kwargs)


class WorkoutDialogLayout(MDBoxLayout):
    def __init__(self, *args, workouts=None, width=None, widgets=[], **kwargs):
        super(WorkoutDialogLayout, self).__init__(*args, **kwargs)

        self.orientation = "vertical"
        self.adaptive_height = True
        self.spacing = 15
        self.size_hint_x = None
        self.width = width
        self.widgets = widgets

        self.scroll_layout = MDBoxLayout(
            orientation="vertical",
            adaptive_height=True,
            spacing=15,
            padding=20
        )

        self.scroll_view = MDScrollView(
            always_overscroll=True,
            do_scroll_x=False
        )
        self.scroll_view.add_widget(self.scroll_layout)

        # if workouts:
        #     for workout in workouts:
        #         self.scroll_layout.add_widget(workout)
        # else:
        #     print("No workouts")
        # for widget in widgets:
        #     # widget.size_hint_x = None
        #     # widget.adaptive_height = True
        #     # widget.width = self.width
        #     # widget.text_size = widget.size
        #     widget.halign = "center"
        #     self.scroll_layout.add_widget(widget)

        self.add_widget(self.scroll_view)

        self.add_widget(
            MDRaisedButton(
                text="+",
                size_hint_x=None,
                width=self.width,
                on_release=self.add_set
            )
        )

    def add_set(self, *args):
        print("Adding Set")
        self.scroll_layout.add_widget(MDLabel(text='Test Text Field'))
        print("Added Set")

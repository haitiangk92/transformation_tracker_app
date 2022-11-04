from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivymd.uix.card import MDCard
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
from kivymd.uix.list import OneLineRightIconListItem, IRightBody, OneLineListItem

from pprint import pprint

EXAMPLE_WORKOUTS = {
    "Bench Presses": {
        "reps": [5, 5, 5, 5, 5],
        "weight": [135, 140, 145, 140, 135],
        "slow reps": [False, False, False, False, False]
    },
    "T-Curls": {
        "reps": [10, 10, 10],
        "weight": [155, 165, 155],
        "slow reps": [False, False, False]
    },
    "Dips": {
        "reps": [10, 10, 10],
        "weight": [225, 225, 225],
        "slow reps": [False, False, False]
    }
}

EXAMPLE_USERNAME = "User"


class PRMax(IRightBody, MDBoxLayout):
    'Custom Right Contianer'


class PersonalRecord(OneLineRightIconListItem):
    '''Personal Record'''

    def __init__(self, *args, workout=None, **kwargs):
        super(PersonalRecord, self).__init__(*args, **kwargs)

        # workout_name = self.ids.workout_name
        label = self.ids.label

        if not workout:
            self.text = "No Workout"
            return

        name, meta = workout

        self.text = name
        label.text = str(max(meta['weight']))


class WorkoutDesc(MDBoxLayout):
    '''Workout Description'''

    def __init__(self, workout=None, **kwargs):
        super(WorkoutDesc, self).__init__(**kwargs)

        header = self.ids.header
        sets = self.ids.sets

        if not workout:
            header.add_widget(MDLabel(text="No Workout"))
            return

        for key in workout.keys():
            self.add_new_label(header, key.title())

        sets.cols = len(workout.keys())

        for i in range(len(workout[list(workout.keys())[0]])):
            for key in workout.keys():
                self.add_new_label(sets, str(workout[key][i]))

    def add_new_label(self, widget, string):
        added_label = MDLabel(
            text=string,
            halign="center",
            size_hint_y=None,
            height=25
        )

        added_label.text_size = added_label.size
        widget.add_widget(added_label)


class DashboardCard(MDCard):
    '''DASHBOARD CARD'''


class NavDashboard(Widget):
    '''NAV DASHBOARD'''

    # kv file loader
    Builder.load_file("styles/dashboard.kv")

    last_session_workouts = EXAMPLE_WORKOUTS
    workouts = EXAMPLE_WORKOUTS
    username = EXAMPLE_USERNAME

    greeting = ObjectProperty(None)
    last_session = ObjectProperty(None)
    personal_records = ObjectProperty(None)

    def on_greeting(self, *args):
        self.greeting.text = f"Hello {self.username}"

    def on_last_session(self, *args):
        for workout in self.last_session_workouts:
            self.last_session.ids.list_id.add_widget(
                MDExpansionPanel(
                    icon="",
                    content=WorkoutDesc(
                        workout=self.last_session_workouts[workout]
                    ),
                    panel_cls=MDExpansionPanelOneLine(
                        text=f"   {workout}"
                    )
                )
            )

    def on_personal_records(self, *args):
        list_id = self.personal_records.ids.list_id
        limit = 4

        for i in range(3):
            list_id.add_widget(
                PersonalRecord(
                    workout=list(self.workouts.items())[i]
                )
            )

        if len(self.workouts) > 2:
            list_id.add_widget(
                OneLineListItem(
                    text="See More ..."
                )
            )

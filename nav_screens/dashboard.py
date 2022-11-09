from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivymd.uix.card import MDCard
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
from kivymd.uix.list import OneLineRightIconListItem, IRightBody, OneLineListItem
from kivymd.uix.dialog import MDDialog

from pprint import pprint
from datetime import datetime

EXAMPLE_WORKOUTS = {
    "Bench Presses": {
        "type": "Weight",
        "reps": [5, 5, 5, 5, 5],
        "weight": [135, 140, 145, 140, 135],
        "slow_reps": [False, False, False, False, False]
    },
    "T-Curls": {
        "type": "Weight",
        "reps": [10, 10, 10],
        "weight": [155, 165, 155],
        "slow_reps": [False, False, False]
    },
    "Dips": {
        "type": "Body",
        "reps": [10, 10, 10],
        "weight": [225, 225, 225],
        "slow_reps": [False, False, False]
    },
    "Swimming": {
        "type": "Cardio",
        "reps": [20],
        "weight": None,
        "slow_reps": None
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
        weights = meta['weight']

        self.text = name
        label.text = str(
            max(meta['reps']) if not weights else str(max(weights)) + " lbs")


class WorkoutDesc(MDBoxLayout):
    '''Workout Description'''

    def __init__(self, workout=None, **kwargs):
        super(WorkoutDesc, self).__init__(**kwargs)

        header = self.ids.header
        sets = self.ids.sets

        if not workout:
            header.add_widget(MDLabel(text="No Workout"))
            return

        workout.pop("type")

        for key in workout.keys():
            self.add_new_label(header, key.title())

        sets.cols = len(workout.keys())

        for i in range(len(workout[list(workout.keys())[0]])):
            for key in workout.keys():
                workout_meta = workout[key]
                self.add_new_label(
                    sets, str(None if not workout_meta else workout_meta[i]))

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


class Workout:
    def __init__(self, name):
        self.name - name


class WorkoutSession:
    def __init__(self):
        self.date = datetime.today().strftime()
        self.workouts = []

    def add_workout(self, workout):
        self.workouts.append(workout)

    def close_session(self):
        # Push session to db
        pass


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
    option_3 = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(NavDashboard, self).__init__(**kwargs)

        self.speed_dial_data = {
            "Weight In": [
                "scale"
                "on_press", lambda x: self.add_weigh_in()
            ],
            "Add Workout": [
                "dumbbell"
                "on_press", lambda x: self.add_workout()
            ]
        }

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
        limit = 3

        workout_list = list(self.workouts.items())
        workout_list.sort()

        for i in range(limit):
            list_id.add_widget(
                PersonalRecord(
                    workout=workout_list[i]
                )
            )

        if len(self.workouts) > limit:
            list_id.add_widget(
                OneLineListItem(
                    text="See More ..."
                )
            )

    def add_workout(self):
        print("Adding Workout")

    def add_weigh_in(self):
        print("Weighing in")

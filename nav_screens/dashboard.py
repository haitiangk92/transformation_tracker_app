from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivymd.uix.card import MDCard
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
from kivymd.uix.list import OneLineRightIconListItem, IRightBody, OneLineListItem
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

from widgets.workout_dialog import *
from widgets.workout import *
from widgets.circuit_dialog import *


from pprint import pprint
from datetime import datetime


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

        weights = workout.weight

        self.text = workout.name
        label.text = str(max(workout.reps)
                         if not weights else str(max(weights)) + " lbs")


class WorkoutDesc(MDBoxLayout):
    '''Workout Description'''

    def __init__(self, workout=None, **kwargs):
        super(WorkoutDesc, self).__init__(**kwargs)

        header = self.ids.header
        sets = self.ids.sets

        if not workout:
            header.add_widget(MDLabel(text="No Workout"))
            return

        workout_dict = workout.__dict__
        temp_name = workout_dict.pop("name")
        workout_dict.pop("workout_type")

        for key in workout_dict.keys():
            self.add_new_label(header, key.title())

        sets.cols = len(workout_dict.keys())

        for i in range(len(workout.reps)):
            for key in workout_dict.keys():
                workout_meta = workout_dict[key]
                self.add_new_label(
                    sets,
                    str(None if not workout_meta else workout_meta[i])
                )

        workout_dict["name"] = temp_name

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


class WorkoutSession:
    def __init__(self):
        self.date = datetime.today().strftime()
        self.workouts = []

    def add_workout_dialog(self, workout):
        self.workouts.append(workout)

    def close_session(self):
        # Push session to db
        pass


EXAMPLE_WORKOUTS = [
    Workout(
        "Bench Presses",
        workout_type=WorkoutType.WEIGHT,
        reps=[5, 5, 5, 5, 5],
        weight=[135, 140, 145, 140, 135],
        slow_reps=[False, False, False, False, False]
    ),
    Workout(
        "T-Curls",
        WorkoutType.WEIGHT,
        reps=[10, 10, 10],
        weight=[155, 165, 155],
        slow_reps=[False, False, False]
    ),
    Workout(
        "Dips",
        workout_type=WorkoutType.BODY,
        reps=[10, 10, 10],
        weight=[225, 225, 225],
        slow_reps=[False, False, False]
    ),
    Workout(
        "Swimming",
        workout_type=WorkoutType.CARDIO,
        reps=[20],
        slow_reps=None
    )
]


class NavDashboard(Widget):
    '''NAV DASHBOARD'''

    # kv file loader
    Builder.load_file("styles/dashboard.kv")

    last_session_workouts = EXAMPLE_WORKOUTS
    workouts = EXAMPLE_WORKOUTS
    username = EXAMPLE_USERNAME
    current_session = []

    greeting = ObjectProperty(None)
    last_session = ObjectProperty(None)
    personal_records = ObjectProperty(None)
    option_3 = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(NavDashboard, self).__init__(**kwargs)

        self.speed_dial_data = {
            "Circuit Timer": [
                "timer",
                "on_press",
                self.display_circuit_timer
            ],
            "Weight In": [
                "scale-bathroom",
                "on_press",
                self.add_weigh_in_dialog
            ],
            "Add Workout": [
                "dumbbell",
                "on_press",
                self.add_workout_dialog
            ]
        }

    def on_greeting(self, *args):
        self.greeting.text = f"Hello {self.username}"

    def on_last_session(self, *args):
        for workout in self.last_session_workouts:
            self.last_session.ids.list_id.add_widget(
                MDExpansionPanel(
                    icon="",
                    panel_cls=MDExpansionPanelOneLine(
                        text=f"   {workout.name}"
                    ),
                    content=WorkoutDesc(
                        workout=workout
                    )
                )
            )

    def on_personal_records(self, *args):
        list_id = self.personal_records.ids.list_id
        limit = 3

        for i in range(limit):
            list_id.add_widget(PersonalRecord(workout=self.workouts[i]))

        if len(self.workouts) > limit:
            list_id.add_widget(OneLineListItem(text="See More ..."))

    def add_workout_dialog(self, *args):
        print("Showing Workout Dialog")

        EXAMPLE_WIDGETS = [MDLabel(text=f'Test Field {x+1}') for x in range(3)]

        self.workout_dialog = MDDialog(
            title="Add Workout",
            type="custom",
            content_cls=WorkoutDialogLayout(
                widgets=EXAMPLE_WIDGETS,
                width=self.width
            ),
            buttons=[
                MDFlatButton(
                    text="Add",
                    on_release=self.add_workout
                )
            ]
        )
        self.workout_dialog.open()

    def display_circuit_timer(self, *args):
        print("Show Timer")

        EXAMPLE_WIDGETS = [MDLabel(text=f'Test Field {x+1}') for x in range(3)]

        self.timer_dialog = MDDialog(
            title="Circuit Timer",
            type="custom",
            content_cls=CircuitDialogLayout(),
            # buttons=[
            #     MDFlatButton(
            #         text="Add",
            #         on_release=self.add_workout
            #     )
            # ]
        )
        self.timer_dialog.open()

    def add_weigh_in_dialog(self, *args):
        print("Showing Weigh-In Dialog")

    def add_workout(self, *args):
        print("Adding Workout")

    def add_weight_in(self, *args):
        print("Adding Weight-In")

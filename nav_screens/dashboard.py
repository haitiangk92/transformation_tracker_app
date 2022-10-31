from cProfile import label
from pprint import pprint
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivymd.uix.card import MDCard, MDSeparator
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.list import MDList, OneLineListItem
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine

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
            # print(key.title())
            self.add_new_label(header, key.title())

        sets.cols = len(workout.keys())

        for i in range(len(workout[list(workout.keys())[0]])):
            for key in workout.keys():
                # print(workout[key][i])
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
    '''
    def __init__(self, **kwargs):
        super(DashboardCard, self).__init__(**kwargs)

        greeting = self.ids.greeting
        username = "Emmanuel"
        greeting.text = f"Hello {username}"'''


class NavDashboard(Widget):
    # kv file loader
    Builder.load_file("styles/dashboard.kv")

    workouts = EXAMPLE_WORKOUTS

    greeting = ObjectProperty(None)
    last_session = ObjectProperty(None)
    personal_records = ObjectProperty(None)
    blank_space = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(NavDashboard, self).__init__(**kwargs)

        # greeting = self.ids.greeting
        # print(self.ids)
        # username = "Emmanuel"
        # print(greeting)
        # greeting.text = f"Hello {username}"

    # username = "Emmanuel"

    def on_greeting(self, *args):
        # print(self.ids)
        greeting = self.greeting
        username = "Emmanuel"
        greeting.text = f"Hello {username}"

    def on_last_session(self, *args):
        for workout in self.workouts:
            self.last_session.ids.list_id.add_widget(
                MDExpansionPanel(
                    icon="dumbbell",
                    content=WorkoutDesc(workout=self.workouts[workout]),
                    panel_cls=MDExpansionPanelOneLine(
                        text=workout
                    )
                )
            )

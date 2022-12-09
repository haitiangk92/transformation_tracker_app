from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.widget import MDWidget
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivy.properties import ListProperty, NumericProperty
from kivy.lang import Builder


timer_kv = '''
<Timer>
    # timer_txt: timer_txt

    adaptive_height: True     
    canvas.before:
        Color:
            rgba: root.bar_color + [0.8]
        Line: 
            width: root.bar_width
            ellipse: self.x, self.y, self.width/2, self.width/2, 0, 360
            
    MDLabel:
        id: timer_txt
        text: "1:30"
        halign: "center"
        size_hint: None, None
        size: self.parent.size
        text_size: self.size
        font_size: 64
'''


class Timer(MDBoxLayout):
    bar_color = ListProperty([0.8, 0.95, 0.97])
    bar_width = NumericProperty(15)

    Builder.load_string(timer_kv)


class CircuitDialogLayout(MDBoxLayout):
    def __init__(self, *args, **kwargs):
        super(CircuitDialogLayout, self).__init__(*args, **kwargs)

        self.orientation = "vertical"
        self.adaptive_height = True
        self.spacing = 5
        self.padding = [0, 20]

        self.workout_interval_input = MDTextField(hint_text="Workout Interval")
        self.rest_interval_input = MDTextField(hint_text="Rest Interval")

        timer_layout = MDBoxLayout(
            orientation="vertical", adaptive_height=True)
        input_layout = MDBoxLayout(orientation="horizontal", spacing=20)

        input_layout.add_widget(self.workout_interval_input)
        input_layout.add_widget(self.rest_interval_input)

        timer_layout.add_widget(input_layout)

        timer = Timer(
            pos_hint={
                "center_x": .5,
                "center_y": .5
            }
        )
        timer_layout.add_widget(timer)
        self.add_widget(timer_layout)

        self.start_btn = MDRaisedButton(
            text="Start",
            size_hint_x=None,
            width=self.width,
            on_release=self.start_timer
        )
        self.add_widget(self.start_btn)

    def start_timer(self, *args):
        btn_text = "Stop" if self.start_btn.text == "Start" else "Start"
        self.start_btn.text = btn_text
        print(f"Button Text:{btn_text}")

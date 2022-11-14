from enum import Enum

class WorkoutType(Enum):
    WEIGHT = "Weight_lifting"
    CARDIO = "Cardio"
    BODY = "Calisthenics"


class Workout:
    def __init__(self, name, workout_type=None, reps=0, weight=None, **kwargs):
        self.name = name
        self.workout_type = workout_type
        self.reps = reps
        self.weight = weight

        self.__dict__.update(kwargs)

    def __repr__(self):
        return self.name

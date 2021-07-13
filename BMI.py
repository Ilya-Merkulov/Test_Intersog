from Human import Human
from dataclasses import dataclass

@dataclass
class BMI:
    """Class for Body Mass Index using a human's height and weight"""
    human: Human

    def calculate_BMI(self) -> float:
        return self.human.get_weight() / pow((self.human.get_height() / 100), 2)
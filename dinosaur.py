from inspect import _void
from unicodedata import name


class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100

    def attack(self, robot):
        self.robot -= 10
        print(f"{self.name} has attacked {})

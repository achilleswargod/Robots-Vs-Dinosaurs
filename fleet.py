from random import random
from robot import Robot


class Fleet:
    def __init__(self):
        self.robots = []
        self.create_fleet()

    def create_fleet(self):
        t800 = Robot('T-800')
        self.robots.append(t800)

        t850 = Robot('T-850')
        self.robots.append(t850)

        t1000 = Robot('T-1000')
        self.robots.append(t1000)

from random import random
from robot import Robot

t800 = Robot('T-800')
t850 = ('T-850')
t1000 = Robot('T-1000')


class Fleet:
    def __init__(self):
        self.robots = []

    def create_fleet(self):
        self.robots.append(t800)
        self.robots.append(t850)
        self.robots.append(t1000)

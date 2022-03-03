from weapon import Weapon

pulse_rifle = Weapon('Pulse Rifle', 40)


class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = pulse_rifle

    def attack(self, dinosaur):
        pass

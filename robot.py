from weapon import Weapon


class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon()

    def attack_dino(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power
        print(f"{self.name} attacks {dinosaur.type} with {self.weapon.name} for {self.weapon.attack_power} damage. New health is {dinosaur.health}.")


    def weapon(self):
        self.pulse_rifle = Weapon('Pulse Rifle', 40)

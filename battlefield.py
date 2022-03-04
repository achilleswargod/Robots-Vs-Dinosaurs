from fleet import Fleet
from herd import Herd


class Battlefield:
    def __init__(self):
        self.new_fleet = Fleet()
        self.new_herd = Herd()
        self.chosen_dino_index = 0
        self.chosen_robo_index = 0

    def run_game(self):
        self.display_welcome()
        self.battle()

    def display_welcome(self):
        print("LLLLLLLLETS GET READY TO RRRRRUMMMBBBLLLLEEEEE!!!")

    def battle(self):
        while
        self.show_dino_opponent_options()
        self.show_robo_opponent_options()

        self.dino_turn(self.chosen_dino)
        self.robo_turn(self.chosen_robo)

    def dino_turn(self, dinosaur):
        pass

    def robo_turn(self, robot):
        pass

    def show_dino_opponent_options(self):
        # print out the options for the user to choose from
        # have user select a dinosaur
        self.chosen_dino_index = input("Choose a dinosaur: ")

    def show_robo_opponent_options(self):
        pass

    def display_winners(self):
        pass

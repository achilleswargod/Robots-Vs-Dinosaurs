from fleet import Fleet
from herd import Herd


class Battlefield:
    def __init__(self):
        self.herd = Herd()
        self.fleet = Fleet()

    def run_game(self):
        self.display_welcome()
        self.battle()
        print("**********************************************************************************************************************************************\n")
        self.display_winners()

    def display_welcome(self):
        print("**********************************************************************************************************************************************\n")
        print("LLLLLLLLETS GET READY TO RRRRRUMMMBBBLLLLEEEEE!!!\n")
        print("Today we have a fantastic matchup sure enough to get the sci-fi community pumped!\n")
        print("Robots VS Dinosaurs!\n")
        print("**********************************************************************************************************************************************\n")

    def battle(self):
        # a loop checking the size of the lists to determine which side wins
        while len(self.fleet.robots) > 0 and len(self.herd.dinosaurs) > 0:
            self.dino_turn()
            if len(self.fleet.robots) > 0:
                self.robo_turn()

    def dino_turn(self):
        print("\nBelow is a list of Dinos from some childhood movies!: ")
        self.show_dino_opponent_options()
        chosen_dino = int(input("\nWhich Dino will you unleash?: "))

        print("\nChoose the robot who will defend:")
        self.show_robo_opponent_options()
        chosen_robot = int(input("\nWhich Robot will take natures wrath?: "))

        # calls the attack function from dinosaur.py
        self.herd.dinosaurs[chosen_dino].attack_robot(
            self.fleet.robots[chosen_robot])

        # if the attacked robot health reaches zero, remove from the list
        if self.fleet.robots[chosen_robot].health <= 0:
            print(f"{self.fleet.robots[chosen_robot].name} has died")
            self.fleet.robots.remove(self.fleet.robots[chosen_robot])

    def robo_turn(self):
        print("\nBelow is a list of powerful Robots from Star Wars!: ")
        self.show_robo_opponent_options()
        chosen_robot = int(
            input("\nWhich Robot will prove technology is superior?: "))

        print("\nChoose the dinosaur who will defend:")
        self.show_dino_opponent_options()
        chosen_dino = int(
            input("\nWhich dino will show them they're built dif?: "))

        # calls the attack function from robot.py
        self.fleet.robots[chosen_robot].attack_dino(
            self.herd.dinosaurs[chosen_dino])

        # if the attacked dino health reaches zero, remove from the list
        if self.herd.dinosaurs[chosen_dino].health <= 0:
            print(
                f"{self.herd.dinosaurs[chosen_dino].name} was laser beamed! Oh no!")
            self.herd.dinosaurs.remove(self.herd.dinosaurs[chosen_dino])

    def show_dino_opponent_options(self):
        # iterates through a list of the alive dinos names and the number to choose them.
        dino_index = 0
        for dino in self.herd.dinosaurs:
            print(f"Press {dino_index} for {dino.name}")
            dino_index += 1

    def show_robo_opponent_options(self):
        # iterates through a list of the alive robots names and the number to choose them.
        robot_index = 0
        for robot in self.fleet.robots:
            print(f"Press {robot_index} for {robot.name}")
            robot_index += 1

    def display_winners(self):
        print("We have a winner!")
        if len(self.fleet.robots) > 0:
            print("Robots win!")
        else:
            print("Dinosaurs win!")

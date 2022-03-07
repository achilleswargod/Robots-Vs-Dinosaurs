from dinosaur import Dinosaur


class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()

    def create_herd(self):
        blue = Dinosaur('Blue', 60)  # Velociraptor in Jurrasic World
        self.dinosaurs.append(blue)

        rex = Dinosaur('Rex', 60)  # Trex from "We're Back!"
        self.dinosaurs.append(rex)

        godzilla = Dinosaur('Godzilla', 60)
        self.dinosaurs.append(godzilla)

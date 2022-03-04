from dinosaur import Dinosaur


class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()

    def create_herd(self):
        blue = Dinosaur('Blue', 60)  # Velociraptor in Jurrasic World
        rex = Dinosaur('Rex', 60)  # Trex from "We're Back!"
        godzilla = Dinosaur('Godzilla', 60)

        self.dinosaurs.append(blue)
        self.dinosaurs.append(rex)
        self.dinosaurs.append(godzilla)

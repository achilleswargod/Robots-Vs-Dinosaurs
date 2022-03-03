from dinosaur import Dinosaur

blue = Dinosaur('Blue', 60)  # Velociraptor in Jurrasic World
rex = Dinosaur('Rex', 60)  # Trex from "We're Back!"
godzilla = Dinosaur('Godzilla', 60)


class Herd:
    def __init__(self) -> None:
        self.dinosaurs = []

    def create_herd(self):
        self.dinosaurs.append(blue)
        self.dinosaurs.append(rex)
        self.dinosaurs.append(godzilla)

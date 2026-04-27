import random

class MentalState:
    def __init__(self):
        self.stability = 100
        self.repetition = 0
        self.distortion = 0
        self.blame = 0

    def degrade(self):
        self.stability -= random.randint(1, 2)

        if random.random() < 0.25:
            self.distortion += 1

        if random.random() < 0.15:
            self.blame += 1

    def degrade_extra(self):
        self.stability -= random.randint(3, 5)
        self.distortion += 1

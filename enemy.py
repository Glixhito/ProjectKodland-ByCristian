import random

class CognitiveNoise:
    def __init__(self):
        self.active = False

    def maybe_attack(self, state):
        self.active = False

        if random.random() < 0.15:
            self.active = True
            state.stability -= random.randint(1, 2)
            state.distortion += 1

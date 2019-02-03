import random_generators as rg

class player:
    def __init__(self):
        #gender assigned from generator
        self.gender = rg.gender()
        #name assigned from generator with respect to gender
        self.name = rg.name(self.gender)
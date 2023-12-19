import random

class Cars:
    def __init__(self, model, color, speed, year):
        self.model = model
        self.color = color
        self.speed = speed
        self.year = year
    def keys(self):
        possible_keys = ['Car started up', 'Car not started up']
        key = random.choice(possible_keys)
        print(key)


mclaren = Cars('P1', 'Black', 365, 2023)
mclaren.keys()

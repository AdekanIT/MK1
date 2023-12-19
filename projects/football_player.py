class Player:
    def __init__(self, speed, power, accuracy, stamin):
        self.speed = speed
        self.power = power
        self.accuracy = accuracy
        self.stamin = stamin


    
class Goalkeeper(Player):
    def __init__(self, speed, power, accuracy, stamin):
        super().__init__(speed, power, accuracy, stamin)

    def privilagy(self):
        return print('Can take a ball with hand!')

class Defender(Player):
    def __init__(self, speed, power, accuracy, stamin):
        super().__init__(speed, power, accuracy, stamin)

    def privilagy(self):
        return print('Can take a ball from defender and give ball from goalkeeper to semi-defnder or attacker!')
    
class SemiDefender(Player):
    def __init__(self, speed, power, accuracy, stamin):
        super().__init__(speed, power, accuracy, stamin)

    def privilagy(self):
        return print('Can attacing with attacers and going to the center!')
    

class Attacer(Player):
    def __init__(self, speed, power, accuracy, stamin):
        super().__init__(speed, power, accuracy, stamin)

    def privilagy(self):
        return print('Can attacing to the gate, make goals and cick from corner!')
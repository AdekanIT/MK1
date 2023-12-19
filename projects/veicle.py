class Vehicle:
    def __init__(self, brand, model, speed):
        self.brand = brand
        self.model = model
        self.speed = speed


class Car(Vehicle):
    def __init__(self, brand, model, speed):
        super().__init__(brand, model, speed)

    def info_displey(self):
        return f'Brand:{self.brand}, Model:{self.model}, Speed:{self.speed}km/h '
    
class Motorcycle(Vehicle):
    def __init__(self, brand, model, speed):
        super().__init__(brand, model, speed)

    def info_displey(self):
        return f'Brand:{self.brand}, Model:{self.model}, Speed:{self.speed}km/h '
    


mclaren = Car('McLaren', 'P1', 365)
ducati = Motorcycle('Ducati', 'F300', 325)
print(mclaren.info_displey())
print(ducati.info_displey())
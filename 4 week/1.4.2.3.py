class Cars:
    def __init__(self, model, color, speed, year):
        self.model = model
        self.color = color
        self.speed = speed
        self.year = year

mclaren = Cars('P1', 'Black', 365, 2023)
# mclaren = Cars(model = 'P1', color = 'Black', speed = 365, year = 2023)

print(mclaren.model)
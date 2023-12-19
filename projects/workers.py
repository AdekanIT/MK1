class Worker:
    def __init__(self, name, position):
        self.names = name
        self.positions = position


class HR(Worker):
    def __init__(self, name, position):
        super().__init__(name, position)
    def view_positions(self, view_position):
        return view_position.positions
    

jordan = Worker('Jordan', 'Worker')
mike = HR('Mike', 'HR')

print(mike.view_positions(jordan))
    



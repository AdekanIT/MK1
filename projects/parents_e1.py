class Company:
    def __init___(self, employee, rank, name, age):
        self.employee = employee
        self.rank = rank
        self.name = name
        self.age = age

class Manager(Company):
    def __init__(self, employee, rank, name, age, loyalty):
        super().__init__(employee, rank, name, age)
        self.loyalty = loyalty


employee1 = input('Enter your worker: ')
rank1 = int(input('Enter your position: '))
name1 = input('Enter your name: ')
age1 = int(input('Enter your age: '))
loyalty1 = input('Enter your name: ')
manager = Manager(employee=employee1,
            rank=rank1,
            name = name1,
            age=age1,
            loyalty=loyalty1)

print(manager)
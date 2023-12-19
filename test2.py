class Animal:
    def __init__(self, name):
        self.name = name


class Cat(Animal):
    def __init__(self, name ):
        super().__init__(name)

    def make_sound(self):
        return print('Meow-meow')
    
class Cow(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        return print('Mu-Mu')
    

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        return print('Aaf-Aaf')
    


dog = Dog('Dog')
cat = Cat('Cat')
cow = Cow('Cow')
print(dog.name, dog.make_sound())
print(cat.name, cat.make_sound())
print(cow.name, cow.make_sound())
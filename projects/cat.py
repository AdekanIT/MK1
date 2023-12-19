class Animal:
    def __init__(self, name):
        self.name = name


class Cat(Animal):
    def __init__(self, name ):
        super().__init__(name)

    def make_sound(self):
        return 'Meow-meow'
    
class Cow(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        return 'Mu-Mu'
    

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        return 'Woof-woof'
    


dog = Dog('Dog')
print(dog.name,dog.make_sound())

cat = Cat('Cat')
print(cat.name, cat.make_sound())

cow = Cow('Cow')
print(cow.name, cow.make_sound())


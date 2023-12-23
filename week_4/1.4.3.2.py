class Animal:
    def make_sound(self, s):
        print(s)


class Horse(Animal):
    pass


sound = Horse.make_sound

print(sound)
class Car:
    def __init__(self, make, model):
        self.__make = make  # Приватная переменная (инкапсулирована)
        self.__model = model  # Приватная переменная (инкапсулирована)
        self.__speed = 0  # Приватная переменная (инкапсулирована)

    def accelerate(self, increment):
        self.__speed += increment

    def get_speed(self):
        return self.__speed

# Создание объекта
my_car = Car("Toyota", "Camry")

# Изменение скрытых переменных через публичные методы
my_car.accelerate(20)

# Получение значения скрытой переменной через публичный метод
speed = my_car.get_speed()

print(f"The speed of my car is: {speed} km/h")
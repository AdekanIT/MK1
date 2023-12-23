class MyClass:
    def __init__(self, value):
        self.value = value


    @classmethod
    def multiply(cls,value):
        return value**2
    

print(MyClass.multiply(5))
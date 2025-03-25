# Self keyword is mandatory for calling variables nambes into method
# instance and class variables have different purpose
# constructor name should be _init_
# If you don't create constructor, default constructor: def __init__(self):
# new keyword is not required when you create an object


class Calculator:
    num = 100

    # Constructor always start with init
    def __init__(self, a, b):
        self.firstNumber = a
        self.secondNumber = b
        print("I'm calling auto when object is created with no constructor")

    def getData(self):
        print("This is a method inside a Class")

    def Summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num


obj = Calculator(2, 3)
obj.getData()
print(obj.Summation())

obj1 = Calculator(4, 5)
obj1.getData()
print(obj1.Summation())

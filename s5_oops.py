class Calculator:
    num = 100
    # When you don't create a constructor, default constructor will be called: def __init__(self):

    # Constructor always start with init
    def __init__(self):
         print("I'm calling auto when object is created with no constructor")

    def getData(self):
        print("This is a method inside a Class")


obj = Calculator()
obj.getData()
print(obj.num)



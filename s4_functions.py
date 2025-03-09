"""
This module contains simple functions to print greetings.
"""


# Function declaration
def greet_me():
    print("Hello world")


greet_me()


# Adding one parameter
def hello_world(name):
    print("Hello world, my name is " + name)


hello_world("Job Villagran")


# Adding two or more parameters
def world(a, b):
    print(a + b)


world(2, 3)


# Adding two or more parameters ANOTHER way to do it
def wow_moment(a, b):
    return a+b


print(wow_moment(10, 5))

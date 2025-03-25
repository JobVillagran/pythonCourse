"""This is linked withe the test.txt file"""

file = open('test.txt')

print(file.read())   # Read the entire file
# print(file.read(2))  # Read the first 2 characters

# print(file.readline())  # Read the first line, do not use it with read()

file.close()

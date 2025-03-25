""" This is linked withe the test.txt file """
# Print line by line using readline() method

file = open('test.txt')

line = file.readline()
while line != "":
    print(line)
    line = file.readline()

file.close()

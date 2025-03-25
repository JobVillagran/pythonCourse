""" This is linked with the test.txt file """

# Print line by line using readline() method
# The 'r' means read mode

with open('test.txt', 'r') as reader:
    for line in reader.readlines():
        print(line.strip())  # .strip() para quitar el salto de línea "\n"

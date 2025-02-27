print("hello")

a = 3
print(a)

b, c, d = 5, 6.4, 'I know python'
print(b, c, d)

# print("Value is "+b)   // Eso dara error porque python no concatena las
# variables de esa manera.

# Concatenations, different ways
print("{} {}".format("Value is ", b))

# Identifying type of data
print(type(b))
print(type(c))
print(type(d))

# Concatenation of 2 str
j = "hola mundo"
k = "va"
print(j+" como les "+k)

# List
e = [1, 2, 3, 4, "quiero comer empanadas"]
print(e)

# List Specific values

values = [0, 1, 2, 'Job', 4, 5]
print("1.", values[-1])
print("2.", values[0], values[3])
print("3.", [values[i] for i in (0, 4)])
print("4.", values[1:4])
print("5.", values[2:6])

# Inserting Data into the list

values.insert()

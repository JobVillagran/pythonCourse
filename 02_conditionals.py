# if, else
greeting = "Good Morning America!"

if greeting == "Morning":
    print("Condition Matches")
    print("Python it's different")
else:
    print("Condition do not match")

# for loop
object = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in object:
    print(i)

# multiplying by 2
for i in object:
    print(i * 2)

# print range of numbers
print("******** RANGE NUMBERS *********")
for j in range(1, 7):
    print(j)

# print range of numbers
print("******** RANGE NUMBERS 2 *********")
summation = 0
for k in range(1, 6):
    summation = summation + k
print(summation)


"""
How is done:

This script prints the sum of numbers from 1 to 5, showing
each step of the summation process, including the current value,
the operation being performed, and the accumulated result.
################################################################

print("******** RANGE NUMBERS 2 *********")
summation = 0

# Header of the table
print("Round\tValue of k\tOperation\tAccumulated Result")

for k in range(1, 6):
    # Builds the operation as text (e.g., "0 + 1")
    operation = f"{summation} + {k}"
    # Updates the accumulated total
    summation = summation + k
    # Prints each line with values
    print(f"{k}\t{k}\t\t{operation}\t{summation}")

print(f"Total accumulated: {summation}")
"""

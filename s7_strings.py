str = "Job Python"
str1 = "Villagran"
str2 = "PythonCourse"

print(str[0])
print(str[1])
print(str[2])

print(str[0:3])

print(str + str1)  # Concatenation

print(str2 in str)  # Validation if content has the same info(boolean)

print(str.split("P"))  # Split the string

var = str.split("J")
print(var)
print(var[0])  # Extraction

str3 = " Great "
print(str3.strip())     # Remove white spaces on both sides
print(str3.lstrip())    # Remove white spaces on the left
print(str3.rstrip())    # Remove white spaces on the right

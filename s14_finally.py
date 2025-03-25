ItemInCart = 0
# 2 items will be added to the cart

if ItemInCart != 2:
    # raise Exception("Products Cart count not matching")
    pass


assert ItemInCart == 0

try:
    with open("test.txt", "r") as reader:
        reader.read()
except:
    print("Somehow I reached this block because there is a failure " "in the try block")

try:
    with open("test.txt", "r") as reader:
        reader.read()
except Exception as e:
    print(e)

finally:
    print("cleaning up resources")

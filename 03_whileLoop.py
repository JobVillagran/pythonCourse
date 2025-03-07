it = 4

while it > 1:
    print(it)
    it = it - 1
print("While loop")

miau = 4
# Skipping an specific number
while miau > 1:
    if miau != 3:
        print(miau)
    miau = miau - 1
print("While loop with conditional")

et = 10
# Skipping an specific number + break
while et > 1:
    if et == 3:
        break
    print(et)
    et = et - 1
print("While loop with conditional and break")

at = 10
# multiple if statemens using continue(skipped specifyc data)
while at > 1:
    if at == 9:
        at = at - 1
        continue

    if at == 3:
        break
    print(at)
    at = at - 1
print("While loop with conditional and break")

#----------------- break statement --------------

animal = ["Lion", "Tiger", "Cat", "Dog", "Horse"]
for x in animal:
    print(x)
    if x == "Cat":
        break

#----------------- continue statement --------------

fruit = ["Mango", "Apple", "Orange", "Banana"]
for x in fruit:
    if x == "Orange":
        continue
    print(x)    
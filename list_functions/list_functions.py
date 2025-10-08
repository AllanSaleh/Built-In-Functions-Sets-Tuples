
# print(foods[3])

# foods.append("tacos")

# foods.remove("Tea")

# foods.pop()

# foods.pop(1)

# del foods[3]

# print(foods)
# foods.append("tacos")

# print(foods.count('tacos'))

foods = ["tacos", "Tea", "Pizza", "steak", "nachos", "cookies", "noodles","sushi"]

# ------------- Slicing a list ------------
# Slicing is like indexing, however you pass in two indices a start:stop:step
# returns a sublist of all elements between start and stop (start included, stop not included)
print(foods)
sliced_list = foods[2:7:2]

print(f"sliced: {sliced_list}")
print(f"original: {foods}")

sliced_list2 = foods[4:]
print(f"sliced2: {sliced_list2}")

sliced_list3 = foods[:3]
print(f"sliced3: {sliced_list3}")

slicing_sliced = sliced_list2[1:3]
print(f"sliced sliced {slicing_sliced}")


# -------------- Reverse a list -------------
print(foods[::-1])
foods.reverse() #in-place

print(foods)
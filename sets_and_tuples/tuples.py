# Immutable (unchangeable) sequences

# coordinates = (3,4) #CANNOT BE MODIFIED AFTER CREATION
# Perfect for fixed data that should not change

empty_tuple = ()
singleton = (1,)

print(type(singleton))

# Accessing like list
coordinates = (3,4, 5, 6)

three = coordinates[0]
print(three)


first,_, third, forth = coordinates

print(first)
# print(second)
print(third)
print(forth)


foods = ["Pizza", "steak", "nachos", "cookies"]
price = [20, 63.5, 12, 5]

zipped = list(zip(foods, price)) # [(Pizza, 20), (steak, 63.5), (nachos, 12), (cookies, 5)]
print(zipped)

for food, price in zip(foods, price):
  print(food, price)
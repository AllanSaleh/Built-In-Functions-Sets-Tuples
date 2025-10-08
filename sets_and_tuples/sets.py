# Sets are UNIQUE unordered collections

unique_numbers = {1,2,3,4,5}
print(unique_numbers)
duplicated_number = {1,1,2,2,2,3,3,3,3}
print(duplicated_number)

# Sets use curly braces which are shared with dictionaries
# empty set of curly braces => empty dictionary

empty_set = {}
empty_set = set()

print(type(empty_set))


# removing duplicates from a list by converting it to a set
alist = [6,1,1,5,2,5,3,4,4]
set_list = set(alist)
print(set_list)

back_to_list = list(set_list)
print("back to a list", back_to_list)

# Adding and removing from a set
fruits = {'apple', 'orange'}
fruits.add('banana')

fruits.update(['grapes','pears'])

fruits.discard('apple')

print(fruits)

# Comparing sets

set1 = {1,2,3,4}
set2 = {2,4,6,8}

# union = set1 | set2
union = set1.union(set2)

print(union)

# intersection = set1.intersection(set2)
intersection = set1 & set2

print(intersection)

difference = set1 - set2
print(difference)

difference2 = set2.difference(set1)
# difference2 = set2 - set1

print(difference2)


# Real world example

allans_hobbies = {"fitness", "read a book", "hiking", "doing nothing", "photography"}
class_hobbies = {"fitness", "photography", "sleep", "guitar", "eating", "working on cars", "sitting down"}

# common interests
common = allans_hobbies & class_hobbies
print(common)

# allan's hobbies
unique_hobbies = allans_hobbies - class_hobbies
print(unique_hobbies)

unique_hobbies =  class_hobbies - allans_hobbies
print(unique_hobbies)
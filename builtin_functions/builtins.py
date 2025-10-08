numbers = [2,965,3,45,32,86,]
foods = ["tacos", "Tea", "Pizza", "steak", "nachos", "cookies", "noodles","sushi"]


# ----------- Dealing with numbers -----------

print("Numbers:", numbers)
print("Numbers length:", len(numbers))
print("Sum:", sum(numbers))
print("Max:", max(numbers))
print("Min:", min(numbers))
print(f"Average: {sum(numbers)/len(numbers):.2f}")


# ------------ Sorting --------------
print(f"Sorting numbers: {sorted(numbers)}") #out-of-place / non-destructive
print(numbers)

numbers.sort()
print(f"Sorting inplace: {numbers}") #in-place / destructive

print(f"Sorted on strings: {sorted(foods)}")

# --------------- Type Checking ---------------
def analyze_value(value):
  print(f"Value: {value}")
  print(f"Type: {type(value)}")
  print(f"Is string: {isinstance(value, str)}")
  print(f"Is number: {isinstance(value, (int, float))}")

analyze_value(5.2)
# Dictionary allows us to store key value pairs

student = {
  "name": "Maya",
  "age": 22,
  "major": "Computer Science"
}

# Access values
print(student["name"])
print(student.get("ages", "That key doesn't exist"))

# Adding or updating data
student["age"] = 28
student["gpa"] = 3.8


# removing data
removed_property = student.pop("age")
del student["major"]

print("removed:", removed_property)

print(student)

# looping
for key in student:
  print(key,":",student[key])

# print(student.items())
for key, value in student.items():
  print(f"{key} -> {value}")

print(student.values())
for value in student.values():
  print(value)

library = {
  "book1": {"title": "Atomic Habits", "author":"James Clear"},
  "book2": {"title": "Dune", "author":"Frank"},
}

print(library["book2"]["title"])

# library["book2"]["title"] = "Brave New World"
# library["book2"]["author"] = "Aldous Huxley"

library["book2"] = {"title": "Brave New World", "author":"Aldous Huxley"}

print(library)
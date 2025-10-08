# Lesson 6: In-Class Assignments
## Built-in Functions and For Loops Deep Dive

**Instructions:** Complete each assignment during class when instructed. You have 8-10 minutes for each assignment.

---

## 📝 Assignment 1: Text Processor
**Topic:** For Loops + String Methods  
**Time:** 10 minutes

Create a function that processes a list of usernames and returns clean, valid usernames.

### Requirements:
1. Remove leading/trailing whitespace
2. Convert to lowercase
3. Remove any usernames shorter than 3 characters
4. Remove any usernames containing spaces

```python
def clean_usernames(raw_usernames):
    """
    Clean a list of usernames:
    1. Remove leading/trailing whitespace
    2. Convert to lowercase
    3. Remove any usernames shorter than 3 characters
    4. Remove any usernames containing spaces
    
    Return: List of clean, valid usernames
    """
    # Your code here
    pass

# Test your function with this data:
usernames = ["  Alice123  ", "BOB", "charlie brown", "DIANA_2024", " xy ", "  ERIC  "]
result = clean_usernames(usernames)
print(f"Clean usernames: {result}")

# Expected output: ['alice123', 'bob', 'diana_2024', 'eric']
```

### Test Cases:
- `"  Alice123  "` → `"alice123"` (trimmed and lowercased)
- `"BOB"` → `"bob"` (lowercased)
- `"charlie brown"` → removed (contains space)
- `"DIANA_2024"` → `"diana_2024"` (lowercased)
- `" xy "` → removed (too short after trimming)
- `"  ERIC  "` → `"eric"` (trimmed and lowercased)

---

## 📝 Assignment 2: Quiz Analyzer
**Topic:** Built-in Functions  
**Time:** 10 minutes

Analyze quiz scores and provide comprehensive class statistics.

### Requirements:
1. Calculate class average (rounded to 1 decimal place)
2. Find highest score and corresponding student name
3. Find lowest score and corresponding student name
4. Count how many students scored above average
5. Create a list of students sorted by score (highest to lowest)

```python
def analyze_quiz_scores(student_names, scores):
    """
    Analyze quiz scores and return a summary:
    1. Class average (rounded to 1 decimal)
    2. Highest score and student name
    3. Lowest score and student name
    4. Number of students who scored above average
    5. Students sorted by score (highest to lowest)
    
    Return: Dictionary with analysis results
    """
    # Your code here
    pass

# Test your function with this data:
students = ["Alex", "Sam", "Jordan", "Casey", "Taylor"]
quiz_scores = [78, 94, 82, 67, 91]

result = analyze_quiz_scores(students, quiz_scores)
print(f"Results: {result}")

# Expected structure:
# {
#     'average': 82.4,
#     'highest': (94, 'Sam'),
#     'lowest': (67, 'Casey'),
#     'above_average_count': 2,
#     'sorted_students': [('Sam', 94), ('Taylor', 91), ('Jordan', 82), ('Alex', 78), ('Casey', 67)]
# }
```

### Hints:
- Use `sum()`, `len()`, `max()`, `min()` built-in functions
- Use `zip()` to pair names with scores
- Use `sorted()` with a key parameter for custom sorting

---
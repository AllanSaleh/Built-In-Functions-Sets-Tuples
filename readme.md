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

# Expected output: ['alice123', 'diana_2024', 'eric']
```

### Test Cases:
- `"  Alice123  "` → `"alice123"` (trimmed and lowercased)
- `"BOB"` → `"bob"` (lowercased)
- `"charlie brown"` → removed (contains space)
- `"DIANA_2024"` → `"diana_2024"` (lowercased)
- `" xy "` → removed (too short after trimming)
- `"  ERIC  "` → `"eric"` (trimmed and lowercased)

---
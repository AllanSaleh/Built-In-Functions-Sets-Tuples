def clean_usernames(raw_usernames):
    """
    Clean a list of usernames:
    1. Remove leading/trailing whitespace
    2. Convert to lowercase
    3. Remove any usernames shorter than 3 characters
    4. Remove any usernames containing spaces
    
    Return: List of clean, valid usernames
    """
    new_list = []
    for username in raw_usernames:
        username = username.strip().lower()
        if len(username) >= 3 and ' ' not in username:
            new_list.append(username)
    
    return new_list

# Test your function with this data:
usernames = ["  Alice123  ", "BOB", "charlie brown", "DIANA_2024", " xy ", "  ERIC  "]
result = clean_usernames(usernames)
print(f"Clean usernames: {result}")

# Expected output: ['alice123', 'bob', 'diana_2024', 'eric']
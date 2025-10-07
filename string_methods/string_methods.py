text = "    HeLlo WOrLd!     "

# out-of-place: return modified value, but does not change the original
# in-place: modify the original value

print("before",text)
clean_text = text.strip() # out-of-place
print("after", clean_text)
print(text)

# text = "&%()    HeLlo WOrLd!  ()%&$   "

# print("before",text)
# print("after", text.strip("!@#$%^&*() "))

print(text.lower()) #out of place
print("original:", text)

print("upper", text.upper()) #out of place
print("original:", text)

print("title", text.title()) #out of place
print("original:", text)



# --------- String Testing --------------

passcode = "452069"
print(passcode.isdigit()) #returns true/false value depending on whether or not a string is comprised entirely of digits

name = "AllanAhmed"
print(name.isalpha()) #returns true/false value depending on whether or not a string is comprised entirely of alphabetical characters (Be careful spaces)

username = "allan123%"
print(username.isalnum())


# --------------- Searching --------------

sentence = "Python-is-fun-and-Python-is-powerful"
print(sentence.count("Python")) #returns the amount of times a substring appears in a string (CASE SENSITIVE)

print(sentence.find("power")) #returns the starting index of the substring

# ============= Splitting and Joining =============
words = sentence.split("-") #Splits a string into a list of words, default is to split on every space
print(words)

joined_words = " ".join(words) #Join strings in a list into a single strin, strings separated by whatever character is before .join()

print(joined_words)

# ------------ Membership checks ------------------

sentence = "Python-is-fun-and-Python-is-powerful"

print("*" in sentence)

if '-' in sentence:
  print("WE HAVE HYPHENS")
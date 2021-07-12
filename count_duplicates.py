"""Count the number of Duplicates
Write a function that will return the count of distinct case-insensitive alphabetic characters and 
numeric digits that occur more than once in the input string. The inputstring can be assumed to contain 
only alphabets (both uppercase and lowercase) and numeric digits."""

# My answer:
def duplicate_count(text):
    b = [i.lower() for i in text]
    a = set(b)
    c = 0
    for i in a:
        if b.count(i)>1:
            c +=1
    return c

# Shortest answers by other players:
def duplicate_count(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])
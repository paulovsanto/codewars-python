# Simple, given a string of words, return the length of the shortest word(s).

# String will never be empty and you do not need to account for different data types.

#My answer:
def find_short(s):
    b = s.split()
    c = len(b[0])
    print(c)
    for i in b:
        if len(i) < c:
            c = len(i)
        else:
            None
    return c
#Other players answers:
def find_short(s):
    return min(len(x) for x in s.split())
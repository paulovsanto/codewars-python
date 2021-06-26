# An isogram is a word that has no repeating letters, consecutive or 
# non-consecutive. Implement a function that determines whether a string
# that contains only letters is an isogram. Assume the empty string is an
# isogram. Ignore letter case.

#My answer:
def is_isogram(string):
    b = None
    if string == b:
        return True
    call = string[:]
    cal = call.lower()
    a = ''
    if len(cal) == 0:
        return True 
    elif len(cal) >=1:
        for i in cal:
            if i in a:
                return False
            else:
                a = a+i
    if len(a) == len(cal):
        return True

#Other players answers
def is_isogram(string):
    return len(string) == len(set(string.lower()))
"""Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces."""

#My answer:
def get_count(a):
    return len([i for i in a if i in "aeiou"])
#First time my answer was actually the shortest possible
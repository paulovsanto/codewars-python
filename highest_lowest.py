"""In this little assignment you are given a string of space separated numbers, and have to return the 
highest and lowest number.
Notes:

-All numbers are valid Int32, no need to validate them.
-There will always be at least one number in the input string.
-Output string must be two numbers separated by a single space, and highest number is first."""

#My answer
def high_and_low(numbers):
    a = [int(i) for i in numbers.split()]
    return str(max(a))+" "+str(min(a))

#Not shorter than mine but I liked the format usage
def high_and_low(numbers): #z.
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))
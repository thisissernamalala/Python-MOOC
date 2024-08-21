# Write your solution here
def longest(strings: list):
    num = 0
    for i in strings:
        if len(i)>num:
            num = len(i)
            val = i
    return(val)
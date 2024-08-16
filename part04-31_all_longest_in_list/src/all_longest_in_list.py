# Write your solution here

def all_the_longest(list):
    long = []
    result = []
    for i in list:
        long.append(len(i))
    longest = max(long)

    for j in list:
        if len(j) == longest:
            result.append(j)
    return result

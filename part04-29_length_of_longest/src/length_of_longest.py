# Write your solution here

def length_of_longest(list):
    lenn = []
    for i in list:
        lenn.append(len(i))
        
    return max(lenn)

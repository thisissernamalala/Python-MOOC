# Write your solution here

def sum_of_positives(list):
    s = 0
    for i in list:
        if i>0:
            s+=i
    return s
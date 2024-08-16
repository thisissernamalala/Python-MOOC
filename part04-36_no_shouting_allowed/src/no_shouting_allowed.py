# Write your solution here

def no_shouting(list):
    l = []
    for i in list:
        if i.isupper() == False:
            l.append(i)
    return l
    

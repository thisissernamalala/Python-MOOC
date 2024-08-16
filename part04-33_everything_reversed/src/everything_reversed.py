# Write your solution here\

def everything_reversed(list):
    newl = []
    neww = []
    for i in range(len(list)-1,-1,-1):
        newl.append(list[i])
        print(i)
    print(newl)
    for j in newl:
        neww.append(j[::-1])
    return neww

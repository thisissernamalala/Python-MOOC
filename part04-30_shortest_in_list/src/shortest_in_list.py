# Write your solution here

def shortest(list):
    short = []
    lenn = 0
    for i in list:
        short.append(len(i))
    minn = min(short)
    ind = short.index(minn)

    return list[ind]


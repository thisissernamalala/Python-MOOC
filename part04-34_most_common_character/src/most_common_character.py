# Write your solution here

def most_common_character(string):
    chars = []
    occs = 0
    for i in range(len(string)):
        chars.append(string[i])
    for j in chars:
        cnt = chars.count(j)
        if cnt>occs:
            occs = cnt
            rs = j
    return rs

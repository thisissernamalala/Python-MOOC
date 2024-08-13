# Write your solution here
cur_list = [1, 2, 3, 4, 5]
while True:
    ind = int(input("Index: "))
    if ind == -1:
        break
    else:
        new_val= int(input("New value: "))
        cur_list[ind] = new_val
        print(cur_list)
    

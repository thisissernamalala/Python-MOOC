# Write your solution here
ind = 1
list = []
while True:
    print(f"The list is now {list}")
    inn = input("a(d)d, (r)emove or e(x)it: ")
    if inn == "x":
        print("Bye!")
        break
    elif inn == "d":
        list.append(ind)
        ind+=1
        continue
    elif inn == "r":
        list.pop(-1)
        ind-=1
        continue
        




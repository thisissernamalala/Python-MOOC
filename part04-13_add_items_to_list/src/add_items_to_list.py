# Write your solution here

size= int(input("How many items: "))
list = []
for i in range(1,size+1):
    item = int(input(f"Item {i}: "))
    list.append(item)
print(list)
    
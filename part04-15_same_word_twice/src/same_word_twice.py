# Write your solution here
list = []
num = 0
while True:
    word = input("Word: ")
    
    if word in list:
        print(f"You typed in {num} different words")
        break

    else:
        list.append(word)
        num+=1
        continue


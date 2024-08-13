# Write your solution here
og  = []


while True:
    inn = int(input("New item: "))

    if inn == 0:
        print("Bye!")
        break
    else:
        og.append(inn)
        print(f"The list now: {og}")
        changed = sorted(og)
        print(f"The list in order: {changed}")
        continue

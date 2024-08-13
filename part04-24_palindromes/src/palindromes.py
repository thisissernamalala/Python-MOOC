# Write your solution here
def palindromes(s):
    l1 = []
    l2 = []
    while True:
        l1 = []
        l2 = []
    
        for i in s:
            l1.append(i)
    
        for j in range(len(s)-1,-1,-1):
            l2.append(l1[j])

        if l1 != l2:
            return False
        else:
            return True
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!

l1 = []
l2 = []
while True:
    l1 = []
    l2 = []
    s = input("Please type in a palindrome: ")

    for i in s:
        l1.append(i)
    
    for j in range(len(s)-1,-1,-1):
        l2.append(l1[j])

    if l1 != l2:
        print("that wasn't a palindrome")
    else:
        print(f"{s} is a palindrome!")
        break
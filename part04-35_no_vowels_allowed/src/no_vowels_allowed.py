# Write your solution here

def no_vowels(string):
    neww = ""
    for i in string:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            string.replace(i,"")
        else:
            neww+=i
    return  neww

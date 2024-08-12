# Write your solution here
def same_chars(s,v1,v2):
    maxx = len(s) - 1
    if v1 > maxx or v2 > maxx:
        return False
    elif s[v1] == s[v2]:
        return True
    else:
        return False
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))
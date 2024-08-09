# Write your solution here
def line(i, s):
    if s == "":
        print(int(i)*"*")
    elif len(s)>1:
        print(int(i)*s[0])
    else:
        print(int(i)*s)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")
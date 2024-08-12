# Copy here code of line function from previous exercise
def line(i, s):
    if s == "":
        print(int(i)*"*")
    elif len(s)>1:
        print(int(i)*s[0])
    else:
        print(int(i)*s)
def triangle(size):
    i = 0
    ii = size - 1
    while i<size:
        line(size - ii, "#")
        i+=1
        ii-=1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)

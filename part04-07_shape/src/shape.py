# Copy here code of line function from previous exercise and use it in your solution
def line(i, s):
    if s == "":
        print(int(i)*"*")
    elif len(s)>1:
        print(int(i)*s[0])
    else:
        print(int(i)*s)

def shape(s1,char1,s2,char2):
    i = 0
    ii = 1
    while ii<=s1:
        line(ii,char1)
        ii+=1
        if ii > s1:
            while i<s2:
                line(ii-1,char2)
                i+=1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")


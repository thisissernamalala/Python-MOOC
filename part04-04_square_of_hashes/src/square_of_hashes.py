# Copy here code of line function from previous exercise
def line(i, s):
    if s == "":
        print(int(i)*"*")
    elif len(s)>1:
        print(int(i)*s[0])
    else:
        print(int(i)*s)

def square_of_hashes(size):
    i = 0
    while i<size:
        line(size, "#")
        i+=1
    # You should call function line here with proper parameters
    

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)

# Write your solution here
def greatest_number(a,b,c):
    res = 0
    if a>=b and a>=c:
        res = a
    elif b>=a and b>=c:
        res = b
    elif c>=a and c>=b:
        res = c
    return res
# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)
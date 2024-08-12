# Write your solution here
# def spruce(num):
#     i = 1
#     jump = 1
#     ii = 0
#     while i<=num:
        
#         print((ii+jump)*"*")
#         jump+=1
#         ii+=1
#         i+=1

def spruce(num):
    print("a spruce!")
    j = 0
    k = 1
    sp = num -1
    lssp = num -1 
    while j<num:
        i = (2*k) - 1
        print(sp*" "+i*"*"+sp*" ")
        j+=1
        k+=1
        sp-=1
    print(lssp*" "+"*"+lssp*" " )
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)
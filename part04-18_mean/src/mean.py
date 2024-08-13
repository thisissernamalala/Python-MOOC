# Write your solution here
def mean(list):
    length = len(list)
    summ = sum(list)
    av = summ/length
    return av
# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = mean(my_list)
    print(result)
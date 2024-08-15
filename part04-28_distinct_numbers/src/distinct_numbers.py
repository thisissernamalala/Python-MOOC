# Write your solution here

def distinct_numbers(list):
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
    final_list = sorted(new_list)
    return final_list

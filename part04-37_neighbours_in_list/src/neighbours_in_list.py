# Write your solution here

def longest_series_of_neighbours(list):
    current_count = 1
    max_count = 0
    longg = []

    for i in range(len(list)):
        if i < len(list) -1 and (list[i+1] == list[i]+1 or list[i+1] == list[i]-1) :
            print(f"val: {list[i]}")
            current_count += 1
        elif i < len(list) -1 and (list[i+1] != list[i]+1 or list[i+1] != list[i]-1) :
            print(f"val: {list[i]}")
            if current_count>max_count:
                max_count = current_count
            current_count = 1
            
    if current_count>max_count:
        max_count = current_count
    
    return max_count

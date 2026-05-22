

def distinct_list(my_list):
    
    new_list = []

    for item in my_list:
        
        if item not in new_list:
            new_list.append(item)

    return new_list



numbers = [1, 2, 2, 3, 4, 4, 5]


result = distinct_list(numbers)

print("List after removing duplicates:")
print(result)
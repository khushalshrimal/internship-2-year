

def multiply_list(my_list):

    result = 1

    for num in my_list:
        result = result * num

    return result



numbers = [2, 3, 4, 5]


answer = multiply_list(numbers)

print("Multiplication of all numbers is:", answer)
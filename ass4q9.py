def count_letters(text):

    upper = 0
    lower = 0

    for ch in text:

        if ch.isupper():
            upper = upper + 1

        elif ch.islower():
            lower = lower + 1

    print("Upper case letters:", upper)
    print("Lower case letters:", lower)


string = input("Enter a string: ")

count_letters(string)
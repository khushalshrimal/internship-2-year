def check_range(num, start, end):

    if num >= start and num <= end:
        print("Number is within the range")

    else:
        print("Number is outside the range")


number = int(input("Enter number: "))
start = int(input("Enter starting range: "))
end = int(input("Enter ending range: "))

check_range(number, start, end)
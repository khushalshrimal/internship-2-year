def check_prime(num):

    if num <= 1:
        print("Not Prime")

    else:

        for i in range(2, num):

            if num % i == 0:
                print("Not Prime")
                break

        else:
            print("Prime")


number = int(input("Enter a number: "))

check_prime(number)
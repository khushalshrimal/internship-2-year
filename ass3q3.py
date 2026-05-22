n = int(input("Enter a number: "))
original = n
reverse = 0
while n > 0:
    d = n % 10
    reverse = reverse * 10 + d
    n = n // 10
if original == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")

string1 = input("Enter first string: ")
string2 = input("Enter second string: ")


new_string = string1 + string2


print("\nConcatenated String :", new_string)

# String methods
print("\nLower Case :", new_string.lower())

print("Upper Case :", new_string.upper())

print("Title Case :", new_string.title())

print("Swap Case :", new_string.swapcase())

print("Capitalize :", new_string.capitalize())

print("Casefold :", new_string.casefold())

print("Center :", new_string.center(30))

print("Count of 'a' :", new_string.count('a'))

print("Ends with 'a' :", new_string.endswith('a'))

print("Find 'a' :", new_string.find('a'))

print("Is Alphanumeric :", new_string.isalnum())

print("Is Digit :", new_string.isdigit())

print("Is Numeric :", new_string.isnumeric())

print("Is Space :", new_string.isspace())

print("Replace a with @ :", new_string.replace('a', '@'))
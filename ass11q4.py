import numpy as np
arr = np.array([[10, 20, 30],[40, 50, 60]])
print("Original Array:")
print(arr)

print("Maximum Value:", np.max(arr))
print("Minimum Value:", np.min(arr))

rows, cols = arr.shape
print("\nNumber of Rows:", rows)
print("Number of Columns:", cols)

print("\nAll Elements:")
print(arr)
print("\nSpecific Element (Row 2, Column 3):")
print(arr[1][2])
total = 0
for row in arr:
    for element in row:
        total += element
print("Sum of All Elements:", total)
arr1 = np.array([10, 20, 30])
arr2 = np.array([1, 2, 3])
print("First Array:", arr1)
print("Second Array:", arr2)

print("\nAddition:")
print(np.add(arr1, arr2))

print("\nSubtraction:")
print(np.subtract(arr1, arr2))

print("\nMultiplication:")
print(np.multiply(arr1, arr2))

print("\nDivision:")
print(np.divide(arr1, arr2))
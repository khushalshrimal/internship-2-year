import numpy as np
arr = np.array([10, -5, 20, -8, 15, -2])

print("Original Array:")
print(arr)

# Replace negative values with 0
arr[arr < 0] = 0

print("\nArray after replacing negative values with 0:")
print(arr)

# Replace negative values with 0
arr = np.where(arr < 0, 0, arr)

print("\nArray after replacement:")
print(arr)
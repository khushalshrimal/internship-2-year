import numpy as np
arr = np.array([10, 20, 30,40, 50, 60])
print("Original Array:")
print(arr)

reverse_arr = arr[::-1]
print("\nReversed Array:")
print(reverse_arr)
arr = np.array([[10, 20, 30],[40, 50, 60]])
print("Original Array:")
print(arr)

reverse_arr = arr[ ::-1, ::-1]
print("\nReversed Array:")
print(reverse_arr)

import numpy as np
arr = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

print("Original 3D Array:")
print(arr)

print("\nShape of Original Array:")
print(arr.shape)
new_arr = np.moveaxis(arr, 0, 2)
print("\nArray after Moving Axes:")
print(new_arr)

print("\nShape after Moving Axes:")
print(new_arr.shape)
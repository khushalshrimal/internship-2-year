import numpy as np
arr = np.array([
    [6, -8, 73, -110],
    [np.nan, -8, 0, 94]
])
print("Original Array:")
print(arr)
arr[np.isnan(arr)] = 0
print("\nArray after replacing NaN with 0:")
print(arr)
transpose_arr = arr.T
print("\nArray after interchanging rows and columns:")
print(transpose_arr)
print("\nFirst 3 Rows and 3 Columns:")
print(transpose_arr[:3, :3])
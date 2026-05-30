import numpy as np

arr1 = np.array([10, 20])
arr2 = np.array([[30, 40],
                 [50, 60]])
print("1D Array:")
print(arr1)
print("\n2D Array:")
print(arr2)
arr1_2d = arr1.reshape(1, 2)
print("1D Array reshaped to 2D:")
print(arr1_2d)

combined_arr = np.vstack((arr1_2d, arr2))
print("\nCombined Array:")
print(combined_arr)

import numpy as np
arr1 = np.array([1, 2, 3, 4, 5, 6])
print("1D Array:")
print(arr1)

arr2 = arr1.reshape(2, 3)
print("\n2D Array:")
print(arr2)
print("Array Attributes:")

print("Shape      :", arr2.shape)
print("Dimension  :", arr2.ndim)
print("Data Type  :", arr2.dtype)
print("Item Size  :", arr2.itemsize, "bytes")
arr3 = np.full((3, 3), 9)
print("3×3 Array of all 9s:")
print(arr3) 
arr1 = np.linspace(25, 125, 10)
print("10 Evenly Spaced Values:")
print(arr1)
my_list = [10, 20, 30, 40, 50]
arr2 = np.array(my_list)
print("NumPy Array from Python List:")
print(arr2)
reverse_arr = arr2[::-1]
print("Reversed Array:")
print(reverse_arr)
arr3 = np.arange(48).reshape(4, 4, 3)
print("4×4×3 Array:")
print(arr3)

value = arr3[1, 0, -1]
print("\nSecond Set, First Row, Last Column Value:")
print(value)
arr4 = np.arange(1, 17).reshape(4, 4)
print("4×4 Array:")
print(arr4)

result = arr4[::2, 1::2]
print("\nOdd Rows and Even Columns:")
print(result)
arr = np.arange(48).reshape(4, 4, 3)
print("4×4×3 Array:")
print(arr)

result = arr[1, :2, :2]
print("\nFirst 2 Rows and First 2 Columns of Second Set:")
print(result)
arr2 = np.array([[23, 56, 78, 93],
                 [71, 82, 13, 24]])
print("Original Array:")
print(arr2)

for i in range(arr2.shape[0]): 
    for j in range(arr2.shape[1]):
        if arr2[i][j] % 2 != 0:
            arr2[i][j] = -1

print("\nArray after replacing odd numbers with -1:")
print(arr2)
arr3 = np.array([1, 0, 2, 0, 3, 0, 4])
indices = np.nonzero(arr3)
print("Indices of Non-Zero Elements:")
print(indices)
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])
print("Array A:", a)
print("Array B:", b)

print("\nAddition:")
print(np.add(a, b))

print("\nMultiplication:")
print(np.multiply(a, b))
arr1 = np.array([15, 20, 25])
arr2 = np.array([10, 40, 37])

dot_product = np.dot(arr1, arr2)
print("Dot Product:")
print(dot_product)
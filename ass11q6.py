import numpy as np
arr1 = np.array([3, 4]) 
arr2 = np.array([1, 0])
print("First Array:", arr1)
print("Second Array:", arr2)

avg = (arr1 + arr2) / 2
print("\nAverage of Arrays:")
print(avg)
arr1 = np.array([[10, 20],
                 [30, 40]])
arr2 = np.array([[50, 60],
                 [70, 80]])
print("First 2D Array:")
print(arr1)
print("\nSecond 2D Array:")
print(arr2)

avg = (arr1 + arr2) / 2
print("\nAverage of Arrays:")
print(avg)
from statistics import mode
combined = np.concatenate((arr1, arr2))

print("Mean:", np.mean(combined))
print("Median:", np.median(combined))
print("Mode:", mode(combined.flatten()))


import numpy as np

arr1 = np.array([[1,2,3],
                 [4,5,6]])

arr2 = np.array([[7,8,9],
                 [10,11,12]])

combined = np.concatenate((arr1, arr2))

print("Combined Array:")
print(combined)

print("Mean =", np.mean(combined))
print("Median =", np.median(combined))

# Average
avg = (arr1 + arr2)/2
print("Average Array:")
print(avg)

from scipy import stats

combined1 = np.array([1,2,2,3,4,5,5,5])

mode = stats.mode(combined1)

print("Mode =", mode.mode)
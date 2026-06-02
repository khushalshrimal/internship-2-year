

import numpy as np

A = np.array([[1,-2,3],
              [-1,3,-1],
              [2,-5,5]])

B = np.array([9,-6,17])

# Method 1
X = np.linalg.solve(A,B)

print("Using linalg.solve:")
print(X)

# Method 2 (Inverse Matrix)
A_inv = np.linalg.inv(A)

X2 = np.dot(A_inv,B)

print("Using Inverse Matrix:")
print(X2)

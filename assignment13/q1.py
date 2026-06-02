#1. Replace NaN with 0 and interchange rows & columns
import numpy as np

a = np.array([[6, -8, 73, -110],
              [np.nan, -8, 0, 94]])

# Replace NaN with 0
a = np.nan_to_num(a, nan=0)

print("After replacing NaN:")
print(a)

# Interchange rows
a[[0,1]] = a[[1,0]]
print("After row interchange:")
print(a)

# Interchange columns 0 and 3
a[:,[0,3]] = a[:,[3,0]]
print("After column interchange:")
print(a)

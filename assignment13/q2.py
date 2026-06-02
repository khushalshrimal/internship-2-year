#2) Move axes of 3D array to new positions
import numpy as np

a = np.arange(24).reshape(2,3,4)

print("Original Shape:", a.shape)

b = np.moveaxis(a, 0, 2)

print("New Shape:", b.shape)
print(b)

import numpy as np
arr3d = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])
print("3D Array:")
print(arr3d)

# Using for loop
print("\nIterating using for loop:")
for block in arr3d:
    for row in block:
        for element in row:
            print(element)

# Using nditer
print("\nIterating using nditer:")
for element in np.nditer(arr3d):
    print(element)


import numpy as np

a = np.array([4,-5,7,-2,-9,10])

a = np.where(a < 0, 0, a)

print(a)

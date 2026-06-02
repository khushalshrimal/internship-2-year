
import numpy as np

a = np.array([[1,2,np.nan],
              [4,np.nan,6],
              [7,8,9]])

col_mean = np.nanmean(a, axis=0)

inds = np.where(np.isnan(a))
a[inds] = np.take(col_mean, inds[1])

print(a)
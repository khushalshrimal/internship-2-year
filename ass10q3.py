import pandas as pd
import numpy as np
data = {
    "Math": [90, 80, np.nan, 70],
    "Science": [85, np.nan, 75, 95]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

df = df.fillna(df.mean())
print("\nDataFrame after replacing NaN with column average:")
print(df)
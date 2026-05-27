
import pandas as pd
data = pd.Series([
    "12-08-2026","11-10-2026","05-06-2026"
])

print(data)

res = pd.to_datetime(data)
print(res)
print(type(res))
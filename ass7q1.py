import pandas as pd
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age": [25, 30, 35, 40, 45],
    "CGPA":[3.5, 3.7, 3.8, 3.6, 3.9]
}

df = pd.DataFrame(data)
df3 = pd.DataFrame(data["Name"])
df2 = pd.Series(data)
print(df,"\n")
print(df2,"\n")
print(df3)

data = [90,85,92,81,87]
ps = pd.Series(data, index = ["english","maths","science","history","geography"])
print("Marks of student:\n",ps)

# Access the elements of a Series in Pandas  
data = [90,82,78,45,77]
df= pd.Series(data, index = ['a','b','c','d','e'])
print(df,"\n")
print(df["b"],"\n")
print(df.iloc[2],"\n")
print(df.iloc[1:3],"\n")
print(type(df))
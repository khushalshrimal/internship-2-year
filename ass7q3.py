import pandas as pd
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Marks": [90, 85, 92]
}

df = pd.DataFrame(data)

print(df,"\n")

for index, row in df.iterrows():
    print(index, row["Name"], row["Marks"])
print("\n")


for row in df.itertuples():
    print(row.Name, row.Marks)
print("\n")
    

for i in range(len(df)):
    print(df.iloc[i]["Name"], df.iloc[i]["Marks"])
print("\n")

for i in df.index:
    print(df.loc[i, "Name"], df.loc[i, "Marks"])
print("\n")

df.apply(lambda row: print(row["Name"], row["Marks"]), axis=1)

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age": [25, 30, 35, 40, 45],
    "CGPA":[3.5, 3.2, 3.8, 3.0, 3.9]
}
df = pd.DataFrame(data)
print(df,"\n")

# drop rows where cgpa is less than 3.5 using condition
filtered_df = df[df["CGPA"]>=3.5]
print(filtered_df)

dropped_df = df[df["CGPA"] < 3.5]
print("\n Dropped rows where cgpa is less than 3.5 :\n", dropped_df)

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age": [25, 30, 35, 40, 45],
    "CGPA":[3.5, 3.2, 3.8, 3.0, 3.9]
}

df = pd.DataFrame(data)
print(df,"\n")
print(df.iloc[2],"\n")

# Limited rows selection with given column
print(df.iloc[1:4]["Name"])

data = {
    "flower": ["rose", "lily", "tulip", "sunflower"],
    "quantity": [10, 18, 15, 12],
    "price($)": [5, 3, 4, 6]
}
df = pd.DataFrame(data)
print(df,"\n")
# drop rows where quantity is less than 15
filtered_df = df[df["quantity"]>=15]
print(filtered_df)

data = {
    "flower": ["rose", "lily", "tulip", "sunflower"],
    "quantity": [10, 18, 15, 12],
    "price($)": [5, 3, 4, 6]
}

df = pd.DataFrame(data)
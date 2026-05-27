import pandas as pd

df1 = pd.DataFrame({
    "ID": [1, 2],
    "Name": ["Aman", "Riya"]
})

df2 = pd.DataFrame({
    "ID": [3, 4],
    "Name": ["Karan", "Simran"]
})

df3 = pd.DataFrame({
    "ID": [1, 2, 3, 4],
    "Marks": [85, 90, 78, 88]
})

concat_df = pd.concat([df1, df2], ignore_index=True)

print("Concatenated DataFrame")
print(concat_df)

merged_df = pd.merge(concat_df, df3, on="ID", how="inner")

print("\nMerged DataFrame")
print(merged_df)

df_join1 = concat_df.set_index("ID")
df_join2 = df3.set_index("ID")

join_result = df_join1.join(df_join2)

print("\nJoin Result")
print(join_result)

print("\nDifference Between join() and merge()")

print("\n1. merge()")
print("Used to join DataFrames using common columns")
print("More flexible")
print("Uses pd.merge()")

print("\n2. join()")
print("Used to join DataFrames using index")
print("Simpler and faster for index-based joining")
print("Uses df.join()")
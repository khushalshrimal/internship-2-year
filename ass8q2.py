import pandas as pd



df1 = pd.DataFrame({
    "ID": [1, 2, 3, 4],
    "Name": ["Aman", "Riya", "Karan", "Simran"]
})

df2 = pd.DataFrame({
    "ID": [2, 3, 4, 5],
    "Marks": [85, 90, 78, 88]
})

print("DataFrame 1")
print(df1)

print("\nDataFrame 2")
print(df2)


inner_merge = pd.merge(df1, df2, on="ID", how="inner")

print("\nINNER MERGE ")
print(inner_merge)



left_join = pd.merge(df1, df2, on="ID", how="left")

print("\n LEFT JOIN ")
print(left_join)

print("\nExplanation:")
print("ID 1 is not present in df2, so Marks becomes NaN.")



right_join = pd.merge(df1, df2, on="ID", how="right")

print("\n RIGHT JOIN ")
print(right_join)

print("\nExplanation:")
print("ID 5 is not present in df1, so Name becomes NaN.")



# Setting ID as index
df1_index = df1.set_index("ID")
df2_index = df2.set_index("ID")

# Joining using index
index_join = df1_index.join(df2_index)

print("\nINDEX BASED JOIN ")
print(index_join)



print("\nDIFFERENCE ")
print("merge() joins using columns")
print("join() joins using index")


df3 = pd.DataFrame({
    "ID": [1, 1, 2, 2],
    "Subject": ["Math", "Science", "Math", "Science"],
    "Marks": [80, 85, 75, 90]
})

df4 = pd.DataFrame({
    "ID": [1, 2, 2],
    "Subject": ["Math", "Math", "Science"],
    "Teacher": ["Sharma", "Verma", "Kapoor"]
})

print("\nDataFrame 3")
print(df3)

print("\nDataFrame 4")
print(df4)

# Merge using multiple columns
multi_merge = pd.merge(df3, df4, on=["ID", "Subject"], how="inner")

print("\n MERGE WITH MULTIPLE KEYS ")
print(multi_merge)



print("\n SUMMARY")
print("Inner Join  -> Keeps only common rows")
print("Left Join   -> Keeps all rows from left DataFrame")
print("Right Join  -> Keeps all rows from right DataFrame")
print("Index Join  -> Joins using index")
print("Multiple Keys Merge -> Uses more than one column")
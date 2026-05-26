import pandas as pd
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age": [25, 30, 35, 40, 45],
    "CGPA":[3.5, 3.7, 3.8, 3.6, 3.9]
}

df = pd.DataFrame(data)
print(df)

data = [
    ["flower","quantity","price($)"],
    ["rose",10,5],
    ["lily",8,3],
    ["tulip",15,4],
    ["sunflower",12,6]
]
df = pd.DataFrame(data[1:], columns=data[0])
print(df)

data = [
    ("emp_name","emp_id","department"),
    ("Alice", 101, "HR"),
    ("Bob", 102, "IT"),
    ("Charlie", 103, "Finance"),
    ("David", 104, "Marketing"),
    ("Eve", 105, "Sales")
]
df = pd.DataFrame(data[1:], columns=data[0])
print(df)

data =[
    {"CITY": "New York", "POPULATION": 8419000, "AREA": 783.8},
    {"CITY": "Los Angeles", "POPULATION": 3980000, "AREA": 1214.9},
    {"CITY": "Chicago", "POPULATION": 2716000, "AREA": 589.6},
    {"CITY": "Houston", "POPULATION": 2328000, "AREA": 1651.1},
    {"CITY": "Phoenix", "POPULATION": 1690000, "AREA": 1340.6}
]
df = pd.DataFrame(data)
print(df)
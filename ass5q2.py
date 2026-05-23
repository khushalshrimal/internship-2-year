import sqlite3

# Connect/Create Database
conn = sqlite3.connect("college.db")

# Create Cursor
cur = conn.cursor()

# Create Student Table
cur.execute("""
CREATE TABLE IF NOT EXISTS student(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    city TEXT
)
""")

# Create Course Table
cur.execute("""
CREATE TABLE IF NOT EXISTS course(
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT,
    duration TEXT
)
""")

# Create Teacher Table
cur.execute("""
CREATE TABLE IF NOT EXISTS teacher(
    teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
    teacher_name TEXT,
    subject TEXT
)
""")

# Insert Data into Student Table
cur.execute("INSERT INTO student(name, age, city) VALUES('Vishnu', 20, 'Jodhpur')")
cur.execute("INSERT INTO student(name, age, city) VALUES('Rahul', 21, 'Jaipur')")
cur.execute("INSERT INTO student(name, age, city) VALUES('Aman', 19, 'Delhi')")

# Insert Data into Course Table
cur.execute("INSERT INTO course(course_name, duration) VALUES('Python', '3 Months')")
cur.execute("INSERT INTO course(course_name, duration) VALUES('Java', '4 Months')")

# Insert Data into Teacher Table
cur.execute("INSERT INTO teacher(teacher_name, subject) VALUES('Sharma Sir', 'Python')")
cur.execute("INSERT INTO teacher(teacher_name, subject) VALUES('Mehta Sir', 'Java')")

# Save Changes
conn.commit()

print("Database, Tables and Records created successfully")

# Display Student Table Data
print("\nStudent Table Data:")
cur.execute("SELECT * FROM student")

rows = cur.fetchall()

for row in rows:
    print(row)

# Close Connection
conn.close()
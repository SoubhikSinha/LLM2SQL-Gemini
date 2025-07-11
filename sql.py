# Lets create the database using "SQLlite"

import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('student.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor() # This is for executing SQL commands

# Creating the table
table_info = """CREATE TABLE IF NOT EXISTS students (
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT
);"""

# Creating the table in the database
cursor.execute(table_info)

# Inserting data into the table
insert_data = """INSERT INTO students (NAME, CLASS, SECTION, MARKS) VALUES
    ('John Doe', '10', 'A', 85),
    ('Jane Smith', '10', 'B', 90),
    ('Emily Johnson', '9', 'A', 78),
    ('Aloo Bonda', '7', 'B', 88),
    ('Lalan Sudheer', '8', 'A', 92);"""

cursor.execute(insert_data) # This will insert the data into the students table

# Displaying all records
print("All records in the students table:")
data = cursor.execute("SELECT * FROM students").fetchall()

for row in data:
    print(row) # This will print all the records in the students table

# Committing the changes
conn.commit()

# Closing the connection
conn.close()
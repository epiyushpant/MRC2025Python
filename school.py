import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
connection_obj = sqlite3.connect('school.db')

# Create a cursor object to interact with the database
cursor_obj = connection_obj.cursor()

# Drop the STUDENTS table if it already exists
cursor_obj.execute("DROP TABLE IF EXISTS STUDENTS")

# SQL query to create the table
table_creation_query = """
    CREATE TABLE STUDENTS (
        Student_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        First_Name CHAR(25) NOT NULL,
        Last_Name CHAR(25),
        Email VARCHAR(255) UNIQUE NOT NULL,
        Grade INT,
        Major VARCHAR(50)
    );
"""

# Execute the table creation query
cursor_obj.execute(table_creation_query)

print("Student Database is Ready")

connection_obj.close()

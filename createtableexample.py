import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
connection_obj = sqlite3.connect('geek.db')

# Create a cursor object to interact with the database
cursor_obj = connection_obj.cursor()

# Drop the GEEK table if it already exists (for clean setup)
cursor_obj.execute("DROP TABLE IF EXISTS GEEK")

# SQL query to create the table
table_creation_query = """
    CREATE TABLE GEEK (
        Email VARCHAR(255) NOT NULL,
        First_Name CHAR(25) NOT NULL,
        Last_Name CHAR(25),
        Score INT
    );
"""

# Execute the table creation query
cursor_obj.execute(table_creation_query)

# Confirm that the table has been created
print("Table is Ready")

# Close the connection to the database
connection_obj.close()
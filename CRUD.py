# Inser sample data to table using sqlite 

import sqlite3
def insert_sample_data():
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('sample_data.db')
    cursor = conn.cursor()

    # Create a sample table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    ''')

    # Insert sample data into the table
    sample_data = [
        ('Alice', 30),
        ('Bob', 25),
        ('Charlie', 35)
    ]
    
    cursor.executemany('INSERT INTO users (name, age) VALUES (?, ?)', sample_data)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    insert_sample_data()
    print("Sample data inserted successfully.")


# This code creates a SQLite database and inserts sample data into a table named 'users'.

# Get the sample data from the table

def get_sample_data():
    # Connect to the SQLite database
    conn = sqlite3.connect('sample_data.db')
    cursor = conn.cursor()

    # Query to select all data from the users table
    cursor.execute('SELECT * FROM users')
    
    # Fetch all results
    rows = cursor.fetchall()

    # Close the connection
    conn.close()
    
    return rows
# if __name__ == "__main__":
#     data = get_sample_data()
#     for row in data:
#         print(row)



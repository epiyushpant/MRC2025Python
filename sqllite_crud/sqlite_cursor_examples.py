# cursor_obj.execute(sql, params)
# Run one SQL statement.

# cursor_obj.executemany(sql, seq_of_params)
# Run the same statement many times with different parameter sets.

# cursor_obj.executescript(sql_script)
# Run multiple SQL statements in one string.

# cursor_obj.fetchone()
# Get the next row from query results.

# cursor_obj.fetchmany(size=n)
# Get the next n rows from query results.

# cursor_obj.fetchall()
# Get all remaining rows from query results.

# cursor_obj.close()
# Close the cursor when you are done.

import sqlite3

"""SQLite cursor examples for execute, executemany, executescript, fetchone, fetchmany, fetchall."""

DB_PATH = "school.db"

def setup_database():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    # executescript runs multiple SQL statements in one string.
    cursor.executescript("""
        DROP TABLE IF EXISTS STUDENT_EXAMPLES;
        CREATE TABLE STUDENT_EXAMPLES (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            grade INTEGER
        );
    """)
    print("Database setup complete.")
    connection.commit()
    cursor.close()
    connection.close()


def example_execute():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    # execute runs one SQL statement and can accept parameters.
    cursor.execute(
        "INSERT INTO STUDENT_EXAMPLES (name, grade) VALUES (?, ?)",
        ("Alice", 90),
    )

    # lastrowid returns the ID of the row just inserted.
    print("execute: lastrowid =", cursor.lastrowid)
    # rowcount returns how many rows were affected by the statement.
    print("execute: rowcount =", cursor.rowcount)

    connection.commit()
    cursor.close()
    connection.close()


def example_executemany():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    students = [
        ("Bob", 85),
        ("Carol", 92),
        ("Dave", 78),
    ]

    # executemany runs the same SQL statement multiple times with different parameters.
    cursor.executemany(
        "INSERT INTO STUDENT_EXAMPLES (name, grade) VALUES (?, ?)",
        students,
    )
    print("executemany: rowcount =", cursor.rowcount)

    connection.commit()
    cursor.close()
    connection.close()


def example_executescript():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    # executescript can execute several SQL commands separated by semicolons.
    cursor.executescript(
        """
        INSERT INTO STUDENT_EXAMPLES (name, grade) VALUES ('Eve', 88);
        UPDATE STUDENT_EXAMPLES SET grade = grade + 5 WHERE name = 'Bob';
        INSERT INTO STUDENT_EXAMPLES (name, grade) VALUES ('Frank', 74);
    """
    )
    print("executescript: inserted rows")

    connection.commit()
    cursor.close()
    connection.close()


def example_fetchone():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("SELECT id, name, grade FROM STUDENT_EXAMPLES WHERE grade >= ?", (85,))

    # fetchone returns the next row from the result set or None if no rows remain.
    row = cursor.fetchone()
    print("fetchone:", row)

    cursor.close()
    connection.close()


def example_fetchmany():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("SELECT id, name, grade FROM STUDENT_EXAMPLES ORDER BY id")

    # fetchmany returns the next N rows from the result set.
    rows = cursor.fetchmany(3)
    print("fetchmany (3 rows):")
    for row in rows:
        print(row)

    cursor.close()
    connection.close()


def example_fetchall():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("SELECT id, name, grade FROM STUDENT_EXAMPLES ORDER BY id")

    # fetchall returns all remaining rows from the result set.
    rows = cursor.fetchall()
    print("fetchall:")
    for row in rows:
        print(row)

    cursor.close()
    connection.close()


def main():
    example_fetchall()
    

if __name__ == "__main__":
    main()



# setup_database()
    # example_execute()
    # example_executemany()
    # example_executescript()
    # example_fetchone()
# example_fetchmany()
    # example_fetchall()

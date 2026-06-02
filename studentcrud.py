import sqlite3

# Connect to database (creates if not exists)
connection_obj = sqlite3.connect('school.db')
cursor_obj = connection_obj.cursor()

# Create table if not exists
cursor_obj.execute("""
    CREATE TABLE IF NOT EXISTS STUDENTS (
        Student_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        First_Name TEXT NOT NULL,
        Last_Name TEXT,
        Email TEXT UNIQUE NOT NULL,
        Grade INT,
        Major TEXT
    );
""")
connection_obj.commit()

# --- CRUD Functions ---

def create_student(first, last, email, grade, major):
    cursor_obj.execute("""
        INSERT INTO STUDENTS (First_Name, Last_Name, Email, Grade, Major)
        VALUES (?, ?, ?, ?, ?)
    """, (first, last, email, grade, major))
    connection_obj.commit()
    print("Student added successfully!")

def read_students():
    cursor_obj.execute("SELECT * FROM STUDENTS")
    rows = cursor_obj.fetchall()
    for row in rows:
        print(row)

def update_student(student_id, new_grade):
    cursor_obj.execute("""
        UPDATE STUDENTS
        SET Grade = ?
        WHERE Student_ID = ?
    """, (new_grade, student_id))
    connection_obj.commit()
    print("Student updated successfully!")

def delete_student(student_id):
    cursor_obj.execute("DELETE FROM STUDENTS WHERE Student_ID = ?", (student_id,))
    connection_obj.commit()
    print("Student deleted successfully!")

# --- Menu-driven program ---
def menu():
    while True:
        print("\n--- Student Database Menu ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student Grade")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            first = input("First Name: ")
            last = input("Last Name: ")
            email = input("Email: ")
            grade = int(input("Grade: "))
            major = input("Major: ")
            create_student(first, last, email, grade, major)

        elif choice == "2":
            read_students()

        elif choice == "3":
            student_id = int(input("Enter Student ID to update: "))
            new_grade = int(input("Enter new grade: "))
            update_student(student_id, new_grade)

        elif choice == "4":
            student_id = int(input("Enter Student ID to delete: "))
            delete_student(student_id)

        elif choice == "5":
            print("Exiting program...")
            break

        else:
            print("Invalid choice, try again.")

menu()

# Close connection when done
connection_obj.close()

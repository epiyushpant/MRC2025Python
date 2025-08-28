import tkinter as tk
from tkinter import messagebox
from db import get_connection

def UpdateStudent():
    win = tk.Toplevel()
    win.title("Update Student Information")
    win.geometry("400x500")
    win.resizable(False, False)

    # Title
    title = tk.Label(win, text="Update Student Information", font=("Helvetica", 16, "bold"))
    title.grid(row=0, column=0, columnspan=2, pady=10)

    # Student ID
    tk.Label(win, text="Student ID:", font=("Helvetica", 10)).grid(row=1, column=0, sticky="e", padx=10, pady=5)
    id_entry = tk.Entry(win, width=30)
    id_entry.grid(row=1, column=1, sticky="w", pady=5)

    # Name
    tk.Label(win, text="New Name:", font=("Helvetica", 10)).grid(row=2, column=0, sticky="e", padx=10, pady=5)
    name_entry = tk.Entry(win, width=30)
    name_entry.grid(row=2, column=1, sticky="w", pady=5)

    # Age
    tk.Label(win, text="New Age:", font=("Helvetica", 10)).grid(row=3, column=0, sticky="e", padx=10, pady=5)
    age_entry = tk.Entry(win, width=30)
    age_entry.grid(row=3, column=1, sticky="w", pady=5)

    # Gender
    tk.Label(win, text="New Gender:", font=("Helvetica", 10)).grid(row=4, column=0, sticky="e", padx=10, pady=5)
    gender_var = tk.StringVar()
    gender_var.set(None)
    gender_frame = tk.Frame(win)
    tk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male").pack(side="left", padx=5)
    tk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female").pack(side="left", padx=5)
    gender_frame.grid(row=4, column=1, sticky="w", pady=5)

    # Faculty
    tk.Label(win, text="New Faculty:", font=("Helvetica", 10)).grid(row=5, column=0, sticky="e", padx=10, pady=5)
    faculty_entry = tk.Entry(win, width=30)
    faculty_entry.grid(row=5, column=1, sticky="w", pady=5)

    # Email
    tk.Label(win, text="New Email:", font=("Helvetica", 10)).grid(row=6, column=0, sticky="e", padx=10, pady=5)
    email_entry = tk.Entry(win, width=30)
    email_entry.grid(row=6, column=1, sticky="w", pady=5)

    # Phone
    tk.Label(win, text="New Phone:", font=("Helvetica", 10)).grid(row=7, column=0, sticky="e", padx=10, pady=5)
    phone_entry = tk.Entry(win, width=30)
    phone_entry.grid(row=7, column=1, sticky="w", pady=5)

    # Subjects
    tk.Label(win, text="New Subjects:", font=("Helvetica", 10)).grid(row=8, column=0, sticky="ne", padx=10, pady=5)
    subjects_frame = tk.Frame(win)
    math_var = tk.BooleanVar()
    sci_var = tk.BooleanVar()
    py_var = tk.BooleanVar()
    tk.Checkbutton(subjects_frame, text="Math", variable=math_var).pack(anchor="w")
    tk.Checkbutton(subjects_frame, text="Science", variable=sci_var).pack(anchor="w")
    tk.Checkbutton(subjects_frame, text="Python", variable=py_var).pack(anchor="w")
    subjects_frame.grid(row=8, column=1, sticky="w", pady=5)

    # Update Button
    tk.Button(win, text="Update", width=20, bg="#4CAF50", fg="white", font=("Helvetica", 10, "bold"), command=lambda: update_record()).grid(row=9, column=0, columnspan=2, pady=20)

    def update_record():
        sid = id_entry.get().strip()
        if not sid:
            messagebox.showerror("Error", "Student ID is required!")
            return

        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("SELECT * FROM students WHERE id=?", (sid,))
            student = cur.fetchone()

            if not student:
                messagebox.showerror("Error", "Student not found!")
                return

            new_name = name_entry.get().strip() or student[1]
            new_age = age_entry.get().strip() or student[2]
            new_gender = gender_var.get() or student[3]
            new_faculty = faculty_entry.get().strip() or student[4]
            new_email = email_entry.get().strip() or student[5]
            new_phone = phone_entry.get().strip() or student[6]

            subjects = []
            if math_var.get():
                subjects.append("Math")
            if sci_var.get():
                subjects.append("Science")
            if py_var.get():
                subjects.append("Python")
            new_subjects = ", ".join(subjects) if subjects else student[7]

            cur.execute("""
                UPDATE students 
                SET name=?, age=?, gender=?, faculty=?, email=?, phone=?, subjects=? 
                WHERE id=?
            """, (new_name, new_age, new_gender, new_faculty, new_email, new_phone, new_subjects, sid))
            conn.commit()

            messagebox.showinfo("Success", "Student updated successfully!")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Database Error", f"Error while updating: {e}")
        finally:
            if conn:
                conn.close()

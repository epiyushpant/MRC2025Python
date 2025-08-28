import tkinter as tk
from tkinter import messagebox, ttk
from db import get_connection

def CreateStudent():
    win = tk.Toplevel()
    win.title("Create Student")
    win.geometry("360x500")
    win.configure(bg="#f4f6f7")
    win.resizable(False, False)

    title = tk.Label(
        win, text="Add New Student", 
        font=("Arial", 18, "bold"), 
        bg="#34495e", fg="white", 
        pady=10
    )
    title.pack(fill="x")

    form_frame = tk.Frame(win, bg="#f4f6f7", padx=20, pady=20)
    form_frame.pack(fill="both", expand=True)

    # Labels & Inputs
    tk.Label(form_frame, text="Name:", font=("Arial", 12), bg="#f4f6f7").grid(row=0, column=0, sticky="w", pady=5)
    name_entry = ttk.Entry(form_frame, width=40)
    name_entry.grid(row=0, column=1, pady=5)

    tk.Label(form_frame, text="Age:", font=("Arial", 12), bg="#f4f6f7").grid(row=1, column=0, sticky="w", pady=5)
    age_entry = ttk.Entry(form_frame, width=40)
    age_entry.grid(row=1, column=1, pady=5)

    tk.Label(form_frame, text="Gender:", font=("Arial", 12), bg="#f4f6f7").grid(row=2, column=0, sticky="w", pady=5)
    gender_var = tk.StringVar(value="Male")
    gender_frame = tk.Frame(form_frame, bg="#f4f6f7")
    gender_frame.grid(row=2, column=1, pady=5, sticky="w")
    ttk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male").pack(side="left", padx=5)
    ttk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female").pack(side="left", padx=5)

    tk.Label(form_frame, text="Faculty:", font=("Arial", 12), bg="#f4f6f7").grid(row=3, column=0, sticky="w", pady=5)
    faculty_entry = ttk.Entry(form_frame, width=40)
    faculty_entry.grid(row=3, column=1, pady=5)

    tk.Label(form_frame, text="Email:", font=("Arial", 12), bg="#f4f6f7").grid(row=4, column=0, sticky="w", pady=5)
    email_entry = ttk.Entry(form_frame, width=40)
    email_entry.grid(row=4, column=1, pady=5)

    tk.Label(form_frame, text="Phone:", font=("Arial", 12), bg="#f4f6f7").grid(row=5, column=0, sticky="w", pady=5)
    phone_entry = ttk.Entry(form_frame, width=40)
    phone_entry.grid(row=5, column=1, pady=5)

    # Subjects in a LabelFrame
    subjects_frame = tk.LabelFrame(form_frame, text="Subjects", font=("Arial", 12, "bold"), bg="#f4f6f7", padx=10, pady=10)
    subjects_frame.grid(row=6, column=0, columnspan=2, pady=15, sticky="we")
    math_var = tk.BooleanVar()
    sci_var = tk.BooleanVar()
    py_var = tk.BooleanVar()
    ttk.Checkbutton(subjects_frame, text="Math", variable=math_var).pack(anchor="w")
    ttk.Checkbutton(subjects_frame, text="Science", variable=sci_var).pack(anchor="w")
    ttk.Checkbutton(subjects_frame, text="Python", variable=py_var).pack(anchor="w")

    def submit():
        name = name_entry.get().strip()
        age = age_entry.get().strip()
        gender = gender_var.get()
        faculty = faculty_entry.get().strip()
        email = email_entry.get().strip()
        phone = phone_entry.get().strip()

        subjects = []
        if math_var.get(): subjects.append("Math")
        if sci_var.get(): subjects.append("Science")
        if py_var.get(): subjects.append("Python")

        if not all([name, age, faculty, email, phone]):
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO students (name, age, gender, faculty, email, phone, subjects) 
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (name, age, gender, faculty, email, phone, ", ".join(subjects)))
            conn.commit()
            messagebox.showinfo("Success", "Student added successfully!")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Database Error", f"Error while inserting data: {e}")
        finally:
            if conn:
                conn.close()

    # Submit Button
    submit_btn = tk.Button(win, text="Submit", command=submit, bg="#3498db", fg="white")
    submit_btn.pack(pady=20)

    win.mainloop()

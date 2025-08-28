import tkinter as tk
from tkinter import ttk
from create import CreateStudent
from read import ReadStudent
from update import UpdateStudent
from delete import DeleteStudent
from db import init_db

def main():
    init_db()

    root = tk.Tk()
    root.title("Student Management System (SQLite)")
    root.geometry("500x600")
    root.configure(bg="#f0f4f7")

    # Center Frame
    main_frame = tk.Frame(root, bg="white", bd=2, relief="groove")
    main_frame.place(relx=0.5, rely=0.5, anchor="center", width=400, height=500)

    # Title
    tk.Label(
        main_frame,
        text="Student Management System",
        font=("Arial", 16, "bold"),
        fg="#2c3e50",
        bg="white"
    ).pack(pady=20)

    # Subtitle
    tk.Label(
        main_frame,
        text="Manage students with ease",
        font=("Arial", 10, "italic"),
        fg="#7f8c8d",
        bg="white"
    ).pack(pady=5)

    # Style buttons
    style = ttk.Style()
    style.configure("TButton",
                    font=("Arial", 12),
                    padding=10)
    style.map("TButton",
              background=[("active", "#2980b9")],
              foreground=[("active", "blue")])

    # Buttons
    ttk.Button(main_frame, text="Create Student", width=25, command=CreateStudent).pack(pady=15)
    ttk.Button(main_frame, text="Read Students", width=25, command=ReadStudent).pack(pady=15)
    ttk.Button(main_frame, text="Update Student", width=25, command=UpdateStudent).pack(pady=15)
    ttk.Button(main_frame, text="Delete Student", width=25, command=DeleteStudent).pack(pady=15)

    # Footer / Status
    tk.Label(
        main_frame,
        text="Developed with Tkinter + SQLite",
        font=("Arial", 9),
        fg="#95a5a6",
        bg="white"
    ).pack(side="bottom", pady=15)

    root.mainloop()

if __name__ == "__main__":
    main()

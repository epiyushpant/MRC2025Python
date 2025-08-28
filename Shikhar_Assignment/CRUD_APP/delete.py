import tkinter as tk
from tkinter import messagebox
from db import get_connection

def DeleteStudent():
    win = tk.Toplevel()
    win.title("Delete Student Record")
    win.geometry("400x300")
    win.configure(bg="#f4f6f7")
    win.resizable(False, False)

    # Title
    title = tk.Label(
        win, text="Delete Student", 
        font=("Arial", 16, "bold"), 
        bg="#e74c3c", fg="white", 
        pady=10
    )
    title.pack(fill="x")

    # Form Frame
    form_frame = tk.Frame(win, bg="#f4f6f7", padx=20, pady=20)
    form_frame.pack(expand=True)

    # Student ID Entry
    tk.Label(form_frame, text="Enter Student ID:", font=("Arial", 12), bg="#f4f6f7").grid(row=0, column=0, sticky="w", pady=10)
    id_entry = tk.Entry(form_frame, width=30, font=("Arial", 11))
    id_entry.grid(row=0, column=1, pady=10)

    # Delete button
    def delete_record():
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

            confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete student '{student[1]}'?")
            if not confirm:
                return

            cur.execute("DELETE FROM students WHERE id=?", (sid,))
            conn.commit()

            messagebox.showinfo("Success", "Student deleted successfully!")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Database Error", f"Error while deleting: {e}")
        finally:
            if conn:
                conn.close()

    delete_btn = tk.Button(win, text="Delete Student", command=delete_record, bg="#e74c3c", fg="white", font=("Arial", 11, "bold"), padx=10, pady=5)
    delete_btn.pack(pady=10)

    # Optional: Focus on entry
    id_entry.focus()

import tkinter as tk
from tkinter import ttk, messagebox
from db import get_connection

def ReadStudent():
    win = tk.Toplevel()
    win.title("Read Students")
    win.geometry("900x500")
    
    # Create a frame for the treeview and scrollbar
    frame = tk.Frame(win)
    frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    # Create a treeview with columns
    columns = ("ID", "Name", "Age", "Gender", "Faculty", "Email", "Phone", "Subjects")
    tree = ttk.Treeview(frame, columns=columns, show="headings", height=15)
    
    # Define column headings and widths - ALL LEFT ALIGNED
    column_widths = [20, 120, 20, 50, 120, 180, 80, 200]
    for col, width in zip(columns, column_widths):
        tree.heading(col, text=col, anchor=tk.W)  # Left-align headings
        tree.column(col, width=width, anchor=tk.W)  # Left-align data
    
    # Add scrollbar
    scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    
    # Pack treeview and scrollbar
    tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM students")
        students = cur.fetchall()
        
        if students:
            for student in students:
                tree.insert("", tk.END, values=student)
        else:
            messagebox.showinfo("Info", "No records found!")
            
    except Exception as e:
        messagebox.showerror("Database Error", f"Error while reading data: {e}")
    finally:
        if conn:
            conn.close()
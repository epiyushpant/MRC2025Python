import tkinter as tk
from tkinter import ttk
import sqlite3

# Function to create the database and table if not exists
def create_db():
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS students
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  age INTEGER,
                  gender TEXT,
                  courses TEXT)''')
    conn.commit()
    conn.close()

# Call to create the database at startup
create_db()

class StudentApp:
    def __init__(self, root):
        self.root = root
        root.title("Student Management System")
        root.geometry("800x600")  # Set window size for better layout
        
        # Use ttk for better styling
        self.style = ttk.Style()
        self.style.theme_use('clam')  # Use 'clam' theme for a modern look (alternative to Bootstrap-like styling)
        
        # Configure styles for better GUI appearance
        self.style.configure("TLabel", font=("Helvetica", 12), padding=5)
        self.style.configure("TEntry", font=("Helvetica", 12))
        self.style.configure("TButton", font=("Helvetica", 12, "bold"), padding=10)
        self.style.configure("TRadiobutton", font=("Helvetica", 12))
        self.style.configure("TCheckbutton", font=("Helvetica", 12))
        self.style.configure("Treeview.Heading", font=("Helvetica", 12, "bold"))
        self.style.configure("Treeview", font=("Helvetica", 12), rowheight=25)
        
        # Input Frame for CRUD operations
        input_frame = ttk.LabelFrame(root, text="Student Details", padding=(10, 10))
        input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        
        # Labels and Entries (Textboxes)
        self.name_label = ttk.Label(input_frame, text="Name:")
        self.name_label.grid(row=0, column=0, sticky="w")
        self.name_entry = ttk.Entry(input_frame, width=30)
        self.name_entry.grid(row=0, column=1, pady=5)
        
        self.age_label = ttk.Label(input_frame, text="Age:")
        self.age_label.grid(row=1, column=0, sticky="w")
        self.age_entry = ttk.Entry(input_frame, width=30)
        self.age_entry.grid(row=1, column=1, pady=5)
        
        # Radio Buttons for Gender
        self.gender_label = ttk.Label(input_frame, text="Gender:")
        self.gender_label.grid(row=2, column=0, sticky="w")
        self.gender_var = tk.StringVar(value="Male")
        self.male_radio = ttk.Radiobutton(input_frame, text="Male", variable=self.gender_var, value="Male")
        self.male_radio.grid(row=2, column=1, sticky="w")
        self.female_radio = ttk.Radiobutton(input_frame, text="Female", variable=self.gender_var, value="Female")
        self.female_radio.grid(row=3, column=1, sticky="w")
        self.other_radio = ttk.Radiobutton(input_frame, text="Other", variable=self.gender_var, value="Other")
        self.other_radio.grid(row=4, column=1, sticky="w")
        
        # Checkboxes for Courses
        self.courses_label = ttk.Label(input_frame, text="Enrolled Courses:")
        self.courses_label.grid(row=5, column=0, sticky="w")
        self.python_var = tk.BooleanVar()
        self.java_var = tk.BooleanVar()
        self.cpp_var = tk.BooleanVar()
        self.python_check = ttk.Checkbutton(input_frame, text="Python", variable=self.python_var)
        self.python_check.grid(row=5, column=1, sticky="w")
        self.java_check = ttk.Checkbutton(input_frame, text="Java", variable=self.java_var)
        self.java_check.grid(row=6, column=1, sticky="w")
        self.cpp_check = ttk.Checkbutton(input_frame, text="C++", variable=self.cpp_var)
        self.cpp_check.grid(row=7, column=1, sticky="w")
        
        # ID Entry for Update/Delete
        self.id_label = ttk.Label(input_frame, text="ID (for Update/Delete):")
        self.id_label.grid(row=8, column=0, sticky="w")
        self.id_entry = ttk.Entry(input_frame, width=30)
        self.id_entry.grid(row=8, column=1, pady=5)
        
        # Buttons Frame
        buttons_frame = ttk.Frame(root, padding=(10, 10))
        buttons_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        
        self.add_button = ttk.Button(buttons_frame, text="Add Student", command=self.add_student)
        self.add_button.grid(row=0, column=0, padx=5)
        
        self.update_button = ttk.Button(buttons_frame, text="Update Student", command=self.update_student)
        self.update_button.grid(row=0, column=1, padx=5)
        
        self.delete_button = ttk.Button(buttons_frame, text="Delete Student", command=self.delete_student)
        self.delete_button.grid(row=0, column=2, padx=5)
        
        self.clear_button = ttk.Button(buttons_frame, text="Clear Form", command=self.clear_form)
        self.clear_button.grid(row=0, column=3, padx=5)
        
        # Display Frame with Treeview for viewing records
        display_frame = ttk.LabelFrame(root, text="Student Records", padding=(10, 10))
        display_frame.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky="nsew")
        
        self.tree = ttk.Treeview(display_frame, columns=("ID", "Name", "Age", "Gender", "Courses"), show="headings", height=20)
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Age", text="Age")
        self.tree.heading("Gender", text="Gender")
        self.tree.heading("Courses", text="Courses")
        self.tree.column("ID", width=50)
        self.tree.column("Name", width=150)
        self.tree.column("Age", width=50)
        self.tree.column("Gender", width=100)
        self.tree.column("Courses", width=200)
        self.tree.grid(row=0, column=0, sticky="nsew")
        
        # Scrollbar for Treeview
        scrollbar = ttk.Scrollbar(display_frame, orient="vertical", command=self.tree.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Load initial data
        self.load_data()
        
        # Bind Treeview selection to populate form for update
        self.tree.bind("<<TreeviewSelect>>", self.on_select)
    
    def add_student(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        gender = self.gender_var.get()
        courses = []
        if self.python_var.get(): courses.append("Python")
        if self.java_var.get(): courses.append("Java")
        if self.cpp_var.get(): courses.append("C++")
        courses_str = ", ".join(courses)
        
        if name and age:
            try:
                conn = sqlite3.connect('students.db')
                c = conn.cursor()
                c.execute("INSERT INTO students (name, age, gender, courses) VALUES (?, ?, ?, ?)",
                          (name, int(age), gender, courses_str))
                conn.commit()
                conn.close()
                self.load_data()
                self.clear_form()
            except ValueError:
                tk.messagebox.showerror("Error", "Age must be a number.")
        else:
            tk.messagebox.showerror("Error", "Name and Age are required.")
    
    def update_student(self):
        selected_id = self.id_entry.get()
        if not selected_id:
            tk.messagebox.showerror("Error", "Enter ID to update.")
            return
        
        name = self.name_entry.get()
        age = self.age_entry.get()
        gender = self.gender_var.get()
        courses = []
        if self.python_var.get(): courses.append("Python")
        if self.java_var.get(): courses.append("Java")
        if self.cpp_var.get(): courses.append("C++")
        courses_str = ", ".join(courses)
        
        if name and age:
            try:
                conn = sqlite3.connect('students.db')
                c = conn.cursor()
                c.execute("UPDATE students SET name=?, age=?, gender=?, courses=? WHERE id=?",
                          (name, int(age), gender, courses_str, int(selected_id)))
                conn.commit()
                conn.close()
                self.load_data()
                self.clear_form()
            except ValueError:
                tk.messagebox.showerror("Error", "Age and ID must be numbers.")
        else:
            tk.messagebox.showerror("Error", "Name and Age are required.")
    
    def delete_student(self):
        selected_id = self.id_entry.get()
        if not selected_id:
            tk.messagebox.showerror("Error", "Enter ID to delete.")
            return
        
        try:
            conn = sqlite3.connect('students.db')
            c = conn.cursor()
            c.execute("DELETE FROM students WHERE id=?", (int(selected_id),))
            conn.commit()
            conn.close()
            self.load_data()
            self.clear_form()
        except ValueError:
            tk.messagebox.showerror("Error", "ID must be a number.")
    
    def load_data(self):
        # Clear existing data
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        conn = sqlite3.connect('students.db')
        c = conn.cursor()
        c.execute("SELECT * FROM students")
        rows = c.fetchall()
        for row in rows:
            self.tree.insert("", "end", values=row)
        conn.close()
    
    def clear_form(self):
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.id_entry.delete(0, tk.END)
        self.gender_var.set("Male")
        self.python_var.set(False)
        self.java_var.set(False)
        self.cpp_var.set(False)
    
    def on_select(self, event):
        selected = self.tree.selection()
        if selected:
            item = self.tree.item(selected[0])
            values = item['values']
            self.id_entry.delete(0, tk.END)
            self.id_entry.insert(0, values[0])
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, values[1])
            self.age_entry.delete(0, tk.END)
            self.age_entry.insert(0, values[2])
            self.gender_var.set(values[3])
            courses = values[4].split(", ") if values[4] else []
            self.python_var.set("Python" in courses)
            self.java_var.set("Java" in courses)
            self.cpp_var.set("C++" in courses)

# Main application
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()
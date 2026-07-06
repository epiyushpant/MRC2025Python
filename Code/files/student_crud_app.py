# ============================================
# STUDENT MANAGEMENT CRUD APPLICATION
# ============================================
# Complete application with Create, Read, Update, Delete operations
# Features:
# - Add/Update/Delete students
# - Display students in a table (Treeview)
# - Search and filter
# - Data persistence with JSON
# - Form validation
# ============================================

import tkinter as tk
from tkinter import messagebox, ttk, simpledialog
import json
import os
from datetime import datetime

class StudentCRUDApp:
    """Student Management System using Tkinter"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1000x650")
        
        # Data file for persistence
        self.data_file = "students.json"
        
        # Load data
        self.students = self.load_data()
        
        # Create UI
        self.create_styles()
        self.create_widgets()
        self.refresh_table()
    
    def create_styles(self):
        """Configure Treeview style"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure Treeview colors
        style.configure('Treeview',
                       font=('Arial', 10),
                       rowheight=25)
        style.configure('Treeview.Heading',
                       font=('Arial', 11, 'bold'))
    
    def create_widgets(self):
        """Create all UI widgets"""
        
        # ===== HEADER =====
        header = tk.Frame(self.root, bg="darkblue")
        header.pack(fill=tk.X, padx=0, pady=0)
        
        title = tk.Label(
            header,
            text="📚 Student Management System",
            font=("Arial", 18, "bold"),
            bg="darkblue",
            fg="white",
            pady=15
        )
        title.pack()
        
        # ===== INPUT SECTION =====
        input_frame = tk.LabelFrame(
            self.root,
            text="Student Information",
            font=("Arial", 12, "bold"),
            padx=20,
            pady=15
        )
        input_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Row 1: Name and Roll Number
        tk.Label(input_frame, text="Name:", font=("Arial", 10)).grid(
            row=0, column=0, sticky="w", pady=8
        )
        self.name_entry = tk.Entry(input_frame, font=("Arial", 10), width=25)
        self.name_entry.grid(row=0, column=1, sticky="ew", padx=10, pady=8)
        
        tk.Label(input_frame, text="Roll Number:", font=("Arial", 10)).grid(
            row=0, column=2, sticky="w", pady=8
        )
        self.roll_entry = tk.Entry(input_frame, font=("Arial", 10), width=15)
        self.roll_entry.grid(row=0, column=3, sticky="ew", padx=10, pady=8)
        
        # Row 2: Email and Phone
        tk.Label(input_frame, text="Email:", font=("Arial", 10)).grid(
            row=1, column=0, sticky="w", pady=8
        )
        self.email_entry = tk.Entry(input_frame, font=("Arial", 10), width=25)
        self.email_entry.grid(row=1, column=1, sticky="ew", padx=10, pady=8)
        
        tk.Label(input_frame, text="Phone:", font=("Arial", 10)).grid(
            row=1, column=2, sticky="w", pady=8
        )
        self.phone_entry = tk.Entry(input_frame, font=("Arial", 10), width=15)
        self.phone_entry.grid(row=1, column=3, sticky="ew", padx=10, pady=8)
        
        # Row 3: Department and Grade
        tk.Label(input_frame, text="Department:", font=("Arial", 10)).grid(
            row=2, column=0, sticky="w", pady=8
        )
        self.dept_var = tk.StringVar(value="CSE")
        departments = ["CSE", "ECE", "Mechanical", "Civil", "Electrical"]
        dept_menu = tk.OptionMenu(input_frame, self.dept_var, *departments)
        dept_menu.grid(row=2, column=1, sticky="ew", padx=10, pady=8)
        
        tk.Label(input_frame, text="Grade:", font=("Arial", 10)).grid(
            row=2, column=2, sticky="w", pady=8
        )
        self.grade_var = tk.StringVar(value="A")
        grades = ["A", "B", "C", "D", "F"]
        grade_menu = tk.OptionMenu(input_frame, self.grade_var, *grades)
        grade_menu.grid(row=2, column=3, sticky="ew", padx=10, pady=8)
        
        # Row 4: Address
        tk.Label(input_frame, text="Address:", font=("Arial", 10)).grid(
            row=3, column=0, sticky="nw", pady=8
        )
        self.address_text = tk.Text(input_frame, font=("Arial", 10), height=3, width=60)
        self.address_text.grid(row=3, column=1, columnspan=3, sticky="ew", padx=10, pady=8)
        
        # Configure grid weights
        for i in range(4):
            input_frame.grid_columnconfigure(i, weight=1)
        
        # ===== BUTTON SECTION =====
        button_frame = tk.Frame(self.root)
        button_frame.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Button(
            button_frame,
            text="➕ Add Student",
            command=self.add_student,
            bg="green",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=15,
            pady=8
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            button_frame,
            text="✏️  Update",
            command=self.update_student,
            bg="blue",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=15,
            pady=8
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            button_frame,
            text="🗑️  Delete",
            command=self.delete_student,
            bg="red",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=15,
            pady=8
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            button_frame,
            text="🔄 Clear",
            command=self.clear_fields,
            bg="gray",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=15,
            pady=8
        ).pack(side=tk.LEFT, padx=5)
        
        # Search section
        search_frame = tk.Frame(button_frame)
        search_frame.pack(side=tk.RIGHT, padx=5)
        
        tk.Label(search_frame, text="Search:", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
        self.search_var = tk.StringVar()
        self.search_var.trace("w", self.search_student)
        search_entry = tk.Entry(search_frame, font=("Arial", 10), width=20, textvariable=self.search_var)
        search_entry.pack(side=tk.LEFT, padx=5)
        
        # ===== TABLE SECTION =====
        table_frame = tk.LabelFrame(
            self.root,
            text="Student Records",
            font=("Arial", 12, "bold"),
            padx=5,
            pady=5
        )
        table_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create Treeview
        columns = ("Name", "Roll", "Email", "Phone", "Department", "Grade")
        self.tree = ttk.Treeview(table_frame, columns=columns, height=15, show="headings")
        
        # Define column headings and widths
        column_config = {
            "Name": 150,
            "Roll": 80,
            "Email": 150,
            "Phone": 100,
            "Department": 100,
            "Grade": 60
        }
        
        for col, width in column_config.items():
            self.tree.column(col, width=width, anchor="center")
            self.tree.heading(col, text=col)
        
        # Scrollbars
        vsb = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=self.tree.yview)
        hsb = ttk.Scrollbar(table_frame, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        
        self.tree.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")
        hsb.grid(row=1, column=0, sticky="ew")
        
        table_frame.grid_rowconfigure(0, weight=1)
        table_frame.grid_columnconfigure(0, weight=1)
        
        # Bind row selection
        self.tree.bind("<<TreeviewSelect>>", self.on_row_select)
        
        # ===== STATUS BAR =====
        status_frame = tk.Frame(self.root, bg="lightgray", relief=tk.SUNKEN)
        status_frame.pack(fill=tk.X, padx=0, pady=0)
        
        self.status_label = tk.Label(
            status_frame,
            text="Ready",
            font=("Arial", 10),
            bg="lightgray"
        )
        self.status_label.pack(side=tk.LEFT, padx=10, pady=5)
    
    def add_student(self):
        """Add new student with validation"""
        # Get values
        name = self.name_entry.get().strip()
        roll = self.roll_entry.get().strip()
        email = self.email_entry.get().strip()
        phone = self.phone_entry.get().strip()
        dept = self.dept_var.get()
        grade = self.grade_var.get()
        address = self.address_text.get("1.0", tk.END).strip()
        
        # Validation
        if not all([name, roll, email, phone]):
            messagebox.showerror("Validation Error", "Please fill all required fields!")
            return
        
        # Validate email
        if "@" not in email:
            messagebox.showerror("Validation Error", "Please enter a valid email!")
            return
        
        # Validate phone
        if not phone.isdigit() or len(phone) < 10:
            messagebox.showerror("Validation Error", "Please enter a valid 10-digit phone number!")
            return
        
        # Check duplicate roll number
        if any(s["roll"] == roll for s in self.students):
            messagebox.showerror("Duplicate Error", "Roll number already exists!")
            return
        
        # Create student record
        student = {
            "name": name,
            "roll": roll,
            "email": email,
            "phone": phone,
            "department": dept,
            "grade": grade,
            "address": address,
            "added_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        self.students.append(student)
        self.save_data()
        self.refresh_table()
        self.clear_fields()
        
        self.status_label.config(text=f"✓ Student '{name}' added successfully")
        messagebox.showinfo("Success", f"Student '{name}' added successfully!")
    
    def update_student(self):
        """Update selected student"""
        selected = self.tree.selection()
        
        if not selected:
            messagebox.showerror("Selection Error", "Please select a student to update!")
            return
        
        # Get values
        name = self.name_entry.get().strip()
        roll = self.roll_entry.get().strip()
        email = self.email_entry.get().strip()
        phone = self.phone_entry.get().strip()
        dept = self.dept_var.get()
        grade = self.grade_var.get()
        address = self.address_text.get("1.0", tk.END).strip()
        
        # Validation
        if not all([name, roll, email, phone]):
            messagebox.showerror("Validation Error", "Please fill all required fields!")
            return
        
        # Get student index
        item_id = selected[0]
        index = int(item_id) - 1
        
        # Update
        self.students[index].update({
            "name": name,
            "roll": roll,
            "email": email,
            "phone": phone,
            "department": dept,
            "grade": grade,
            "address": address,
            "updated_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        self.save_data()
        self.refresh_table()
        self.clear_fields()
        
        self.status_label.config(text=f"✓ Student '{name}' updated successfully")
        messagebox.showinfo("Success", f"Student '{name}' updated successfully!")
    
    def delete_student(self):
        """Delete selected student"""
        selected = self.tree.selection()
        
        if not selected:
            messagebox.showerror("Selection Error", "Please select a student to delete!")
            return
        
        item_id = selected[0]
        index = int(item_id) - 1
        student_name = self.students[index]["name"]
        
        # Confirmation
        confirm = messagebox.askyesno(
            "Confirm Delete",
            f"Are you sure you want to delete '{student_name}'?"
        )
        
        if confirm:
            del self.students[index]
            self.save_data()
            self.refresh_table()
            self.clear_fields()
            
            self.status_label.config(text=f"✓ Student '{student_name}' deleted")
            messagebox.showinfo("Success", f"Student '{student_name}' deleted successfully!")
    
    def clear_fields(self):
        """Clear all input fields"""
        self.name_entry.delete(0, tk.END)
        self.roll_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.address_text.delete("1.0", tk.END)
        self.dept_var.set("CSE")
        self.grade_var.set("A")
        self.tree.selection_remove(self.tree.selection())
        self.search_var.set("")
    
    def on_row_select(self, event):
        """Handle row selection - populate fields"""
        selected = self.tree.selection()
        
        if selected:
            item_id = selected[0]
            index = int(item_id) - 1
            student = self.students[index]
            
            # Populate fields
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, student["name"])
            
            self.roll_entry.delete(0, tk.END)
            self.roll_entry.insert(0, student["roll"])
            
            self.email_entry.delete(0, tk.END)
            self.email_entry.insert(0, student["email"])
            
            self.phone_entry.delete(0, tk.END)
            self.phone_entry.insert(0, student["phone"])
            
            self.address_text.delete("1.0", tk.END)
            self.address_text.insert("1.0", student.get("address", ""))
            
            self.dept_var.set(student.get("department", "CSE"))
            self.grade_var.set(student.get("grade", "A"))
    
    def refresh_table(self):
        """Refresh table with current data"""
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Add students
        for i, student in enumerate(self.students, 1):
            self.tree.insert(
                "",
                tk.END,
                iid=str(i),
                values=(
                    student["name"],
                    student["roll"],
                    student["email"],
                    student["phone"],
                    student.get("department", "N/A"),
                    student.get("grade", "N/A")
                )
            )
        
        self.status_label.config(text=f"Total Students: {len(self.students)}")
    
    def search_student(self, *args):
        """Search students by name or roll number"""
        search_term = self.search_var.get().lower()
        
        # Clear table
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Add matching students
        count = 0
        for i, student in enumerate(self.students, 1):
            if (search_term in student["name"].lower() or 
                search_term in student["roll"].lower()):
                self.tree.insert(
                    "",
                    tk.END,
                    iid=str(i),
                    values=(
                        student["name"],
                        student["roll"],
                        student["email"],
                        student["phone"],
                        student.get("department", "N/A"),
                        student.get("grade", "N/A")
                    )
                )
                count += 1
        
        self.status_label.config(text=f"Found: {count} students")
    
    def save_data(self):
        """Save to JSON file"""
        with open(self.data_file, 'w') as f:
            json.dump(self.students, f, indent=4)
    
    def load_data(self):
        """Load from JSON file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            except:
                return []
        return []


# ============================================
# RUN APPLICATION
# ============================================
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentCRUDApp(root)
    root.mainloop()

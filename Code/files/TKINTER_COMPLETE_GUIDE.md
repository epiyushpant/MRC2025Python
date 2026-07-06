# Tkinter Complete Guide: Basics to Intermediate

## Table of Contents
1. [Introduction](#introduction)
2. [Setup & Installation](#setup--installation)
3. [Basics](#basics)
4. [Grid Layout System](#grid-layout-system)
5. [Widgets Deep Dive](#widgets-deep-dive)
6. [Event Handling](#event-handling)
7. [Building CRUD Application](#building-crud-application)

---

## Introduction

Tkinter is Python's standard GUI library. It provides:
- Cross-platform desktop applications
- Simple, intuitive API
- Built-in widgets (buttons, labels, text fields, etc.)
- Flexible layout management (Pack, Grid, Place)

---

## Setup & Installation

### Python Installation
Tkinter comes pre-installed with Python on most systems.

**Verify installation:**
```bash
python -m tkinter
```

If a small window appears, Tkinter is installed. If not, install it:

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install python3-tk
```

**macOS:**
```bash
brew install python-tk@3.x
```

**Windows:**
Tkinter is bundled with Python installer (select it during installation).

---

## Basics

### 1. Creating Your First Window

```python
import tkinter as tk

# Create root window
root = tk.Tk()
root.title("My First App")
root.geometry("400x300")  # width x height

# Keep window open
root.mainloop()
```

**Output:** A 400x300 window with title "My First App"

### 2. Window Properties

```python
import tkinter as tk

root = tk.Tk()

# Window properties
root.title("Window Title")
root.geometry("600x400")  # Set size
root.resizable(True, True)  # Allow/disallow resizing
root.minsize(300, 200)  # Minimum size
root.maxsize(1000, 800)  # Maximum size

# Window icon (uncomment if you have an icon file)
# root.iconbitmap("path/to/icon.ico")

# Background color
root.config(bg="lightblue")

root.mainloop()
```

### 3. Basic Widgets

#### Label
```python
import tkinter as tk

root = tk.Tk()
root.title("Labels Example")
root.geometry("400x200")

label = tk.Label(
    root,
    text="Hello, Tkinter!",
    font=("Arial", 16, "bold"),
    fg="white",
    bg="darkblue",
    pady=10,
    padx=20
)
label.pack()

root.mainloop()
```

#### Button
```python
import tkinter as tk

def on_button_click():
    print("Button was clicked!")

root = tk.Tk()
root.title("Button Example")
root.geometry("400x200")

button = tk.Button(
    root,
    text="Click Me!",
    command=on_button_click,
    font=("Arial", 14),
    bg="green",
    fg="white",
    padx=20,
    pady=10
)
button.pack(pady=20)

root.mainloop()
```

#### Entry (Text Input)
```python
import tkinter as tk

def get_text():
    value = entry.get()
    print(f"You entered: {value}")

root = tk.Tk()
root.title("Entry Example")
root.geometry("400x200")

entry = tk.Entry(
    root,
    font=("Arial", 12),
    width=30
)
entry.pack(pady=10)

# Set placeholder text
entry.insert(0, "Type something...")

button = tk.Button(root, text="Submit", command=get_text)
button.pack(pady=5)

root.mainloop()
```

#### Text Widget (Multi-line)
```python
import tkinter as tk

root = tk.Tk()
root.title("Text Widget Example")
root.geometry("400x300")

text = tk.Text(
    root,
    font=("Arial", 11),
    height=10,
    width=40
)
text.pack(pady=10)

def get_all_text():
    content = text.get("1.0", tk.END)  # Get from line 1, char 0 to END
    print(f"Text content:\n{content}")

button = tk.Button(root, text="Get Text", command=get_all_text)
button.pack()

root.mainloop()
```

---

## Grid Layout System

The Grid layout manager is perfect for creating structured layouts (forms, tables, etc.).

### Grid Basics

```python
import tkinter as tk

root = tk.Tk()
root.title("Grid Layout Example")
root.geometry("400x300")

# Row 0
label1 = tk.Label(root, text="Name:", font=("Arial", 12))
label1.grid(row=0, column=0, sticky="w", padx=10, pady=10)

entry1 = tk.Entry(root, width=30)
entry1.grid(row=0, column=1, padx=10, pady=10)

# Row 1
label2 = tk.Label(root, text="Email:", font=("Arial", 12))
label2.grid(row=1, column=0, sticky="w", padx=10, pady=10)

entry2 = tk.Entry(root, width=30)
entry2.grid(row=1, column=1, padx=10, pady=10)

# Row 2
label3 = tk.Label(root, text="Message:", font=("Arial", 12))
label3.grid(row=2, column=0, sticky="nw", padx=10, pady=10)

text = tk.Text(root, height=5, width=30)
text.grid(row=2, column=1, padx=10, pady=10)

# Buttons at row 3, spanning 2 columns
submit_btn = tk.Button(root, text="Submit", bg="green", fg="white")
submit_btn.grid(row=3, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

root.mainloop()
```

**Key Grid Concepts:**
- `row`: Row number (0-indexed)
- `column`: Column number (0-indexed)
- `columnspan`: Number of columns to span
- `rowspan`: Number of rows to span
- `sticky`: "w" (west/left), "e" (east/right), "n" (north/top), "s" (south/bottom), "ew" (fill horizontal)
- `padx`: Horizontal padding
- `pady`: Vertical padding

### Creating a Form Layout

```python
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Form with Grid")
root.geometry("500x400")

# Title
title = tk.Label(root, text="Registration Form", font=("Arial", 18, "bold"))
title.grid(row=0, column=0, columnspan=2, pady=20)

# Name field
tk.Label(root, text="Name:", font=("Arial", 11)).grid(row=1, column=0, sticky="w", padx=20, pady=10)
name_entry = tk.Entry(root, width=30, font=("Arial", 11))
name_entry.grid(row=1, column=1, padx=20, pady=10)

# Email field
tk.Label(root, text="Email:", font=("Arial", 11)).grid(row=2, column=0, sticky="w", padx=20, pady=10)
email_entry = tk.Entry(root, width=30, font=("Arial", 11))
email_entry.grid(row=2, column=1, padx=20, pady=10)

# Age field
tk.Label(root, text="Age:", font=("Arial", 11)).grid(row=3, column=0, sticky="w", padx=20, pady=10)
age_entry = tk.Entry(root, width=30, font=("Arial", 11))
age_entry.grid(row=3, column=1, padx=20, pady=10)

# Country dropdown
tk.Label(root, text="Country:", font=("Arial", 11)).grid(row=4, column=0, sticky="w", padx=20, pady=10)
country_var = tk.StringVar(root)
country_var.set("Select Country")
countries = ["USA", "UK", "Canada", "India", "Australia"]
country_menu = tk.OptionMenu(root, country_var, *countries)
country_menu.grid(row=4, column=1, sticky="ew", padx=20, pady=10)

# Checkbox
agree_var = tk.BooleanVar()
agree_check = tk.Checkbutton(root, text="I agree to terms", variable=agree_var)
agree_check.grid(row=5, column=0, columnspan=2, padx=20, pady=10)

# Buttons
def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    if name and email:
        messagebox.showinfo("Success", f"Form submitted!\nName: {name}\nEmail: {email}")
    else:
        messagebox.showerror("Error", "Please fill all fields!")

submit_btn = tk.Button(root, text="Submit", command=submit_form, bg="green", fg="white", font=("Arial", 11))
submit_btn.grid(row=6, column=0, sticky="ew", padx=20, pady=20)

clear_btn = tk.Button(root, text="Clear", command=lambda: name_entry.delete(0, tk.END), bg="gray", fg="white", font=("Arial", 11))
clear_btn.grid(row=6, column=1, sticky="ew", padx=20, pady=20)

root.mainloop()
```

---

## Widgets Deep Dive

### 1. Checkbutton
```python
import tkinter as tk

root = tk.Tk()
root.title("Checkbutton Example")
root.geometry("400x200")

var1 = tk.BooleanVar()
var2 = tk.BooleanVar()

cb1 = tk.Checkbutton(root, text="Python", variable=var1)
cb1.pack(pady=5)

cb2 = tk.Checkbutton(root, text="JavaScript", variable=var2)
cb2.pack(pady=5)

def show_selection():
    print(f"Python: {var1.get()}, JavaScript: {var2.get()}")

btn = tk.Button(root, text="Show Selection", command=show_selection)
btn.pack(pady=20)

root.mainloop()
```

### 2. Radiobutton
```python
import tkinter as tk

root = tk.Tk()
root.title("Radiobutton Example")
root.geometry("400x200")

skill_var = tk.StringVar(value="beginner")

rb1 = tk.Radiobutton(root, text="Beginner", variable=skill_var, value="beginner")
rb1.pack(pady=5)

rb2 = tk.Radiobutton(root, text="Intermediate", variable=skill_var, value="intermediate")
rb2.pack(pady=5)

rb3 = tk.Radiobutton(root, text="Advanced", variable=skill_var, value="advanced")
rb3.pack(pady=5)

def show_level():
    print(f"Selected: {skill_var.get()}")

btn = tk.Button(root, text="Show Level", command=show_level)
btn.pack(pady=20)

root.mainloop()
```

### 3. Listbox
```python
import tkinter as tk

root = tk.Tk()
root.title("Listbox Example")
root.geometry("400x300")

listbox = tk.Listbox(root, font=("Arial", 11), height=8)
listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Add items
items = ["Python", "JavaScript", "Java", "C++", "Go", "Rust"]
for item in items:
    listbox.insert(tk.END, item)

def get_selection():
    selected = listbox.curselection()
    if selected:
        item = listbox.get(selected[0])
        print(f"Selected: {item}")

btn = tk.Button(root, text="Get Selection", command=get_selection)
btn.pack(pady=5)

root.mainloop()
```

### 4. Frame
```python
import tkinter as tk

root = tk.Tk()
root.title("Frame Example")
root.geometry("500x300")

# Top frame
top_frame = tk.Frame(root, bg="lightblue", height=100)
top_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

label_top = tk.Label(top_frame, text="Top Section", font=("Arial", 14), bg="lightblue")
label_top.pack(pady=20)

# Middle frame
middle_frame = tk.Frame(root, bg="lightgreen", height=100)
middle_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

label_middle = tk.Label(middle_frame, text="Middle Section", font=("Arial", 14), bg="lightgreen")
label_middle.pack(pady=20)

# Bottom frame
bottom_frame = tk.Frame(root, bg="lightyellow", height=100)
bottom_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

label_bottom = tk.Label(bottom_frame, text="Bottom Section", font=("Arial", 14), bg="lightyellow")
label_bottom.pack(pady=20)

root.mainloop()
```

---

## Event Handling

### 1. Button Click Events
```python
import tkinter as tk

root = tk.Tk()
root.title("Event Handling")
root.geometry("400x200")

def on_click():
    label.config(text="Button was clicked!")

label = tk.Label(root, text="Click the button", font=("Arial", 12))
label.pack(pady=20)

button = tk.Button(root, text="Click Me", command=on_click, font=("Arial", 12))
button.pack(pady=10)

root.mainloop()
```

### 2. Entry Widget Events
```python
import tkinter as tk

root = tk.Tk()
root.title("Entry Events")
root.geometry("400x200")

def on_text_change(event=None):
    text = entry.get()
    label.config(text=f"You typed: {text}")

label = tk.Label(root, text="Type something...", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=10)

# Bind event: 'KeyRelease' triggers on every key press
entry.bind('<KeyRelease>', on_text_change)

root.mainloop()
```

### 3. Button with Parameters
```python
import tkinter as tk
from functools import partial

root = tk.Tk()
root.title("Button with Parameters")
root.geometry("400x200")

def greet(name):
    print(f"Hello, {name}!")

label = tk.Label(root, text="Click any button", font=("Arial", 12))
label.pack(pady=20)

btn1 = tk.Button(root, text="Greet Alice", command=partial(greet, "Alice"))
btn1.pack(pady=5)

btn2 = tk.Button(root, text="Greet Bob", command=partial(greet, "Bob"))
btn2.pack(pady=5)

root.mainloop()
```

---

## Building CRUD Application

A complete CRUD (Create, Read, Update, Delete) application for managing student records.

```python
import tkinter as tk
from tkinter import messagebox, ttk
import json
import os

class StudentCRUDApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("900x600")
        
        # Data file
        self.data_file = "students.json"
        self.students = self.load_data()
        
        # Create UI
        self.create_widgets()
        self.refresh_table()
    
    def create_widgets(self):
        """Create all UI widgets"""
        
        # ===== INPUT FRAME =====
        input_frame = tk.LabelFrame(
            self.root,
            text="Student Details",
            font=("Arial", 12, "bold"),
            padx=20,
            pady=20
        )
        input_frame.pack(fill=tk.BOTH, padx=10, pady=10)
        
        # Name
        tk.Label(input_frame, text="Name:", font=("Arial", 11)).grid(row=0, column=0, sticky="w", pady=5)
        self.name_entry = tk.Entry(input_frame, font=("Arial", 11), width=30)
        self.name_entry.grid(row=0, column=1, sticky="ew", padx=10, pady=5)
        
        # Roll Number
        tk.Label(input_frame, text="Roll Number:", font=("Arial", 11)).grid(row=0, column=2, sticky="w", pady=5)
        self.roll_entry = tk.Entry(input_frame, font=("Arial", 11), width=20)
        self.roll_entry.grid(row=0, column=3, sticky="ew", padx=10, pady=5)
        
        # Email
        tk.Label(input_frame, text="Email:", font=("Arial", 11)).grid(row=1, column=0, sticky="w", pady=5)
        self.email_entry = tk.Entry(input_frame, font=("Arial", 11), width=30)
        self.email_entry.grid(row=1, column=1, sticky="ew", padx=10, pady=5)
        
        # Phone
        tk.Label(input_frame, text="Phone:", font=("Arial", 11)).grid(row=1, column=2, sticky="w", pady=5)
        self.phone_entry = tk.Entry(input_frame, font=("Arial", 11), width=20)
        self.phone_entry.grid(row=1, column=3, sticky="ew", padx=10, pady=5)
        
        # Grade
        tk.Label(input_frame, text="Grade:", font=("Arial", 11)).grid(row=2, column=0, sticky="w", pady=5)
        self.grade_var = tk.StringVar(value="A")
        grade_menu = tk.OptionMenu(input_frame, self.grade_var, "A", "B", "C", "D", "F")
        grade_menu.grid(row=2, column=1, sticky="ew", padx=10, pady=5)
        
        # ===== BUTTON FRAME =====
        button_frame = tk.Frame(input_frame)
        button_frame.grid(row=3, column=0, columnspan=4, pady=20, sticky="ew")
        
        tk.Button(
            button_frame,
            text="Add Student",
            command=self.add_student,
            bg="green",
            fg="white",
            font=("Arial", 11),
            padx=15,
            pady=8
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            button_frame,
            text="Update",
            command=self.update_student,
            bg="blue",
            fg="white",
            font=("Arial", 11),
            padx=15,
            pady=8
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            button_frame,
            text="Delete",
            command=self.delete_student,
            bg="red",
            fg="white",
            font=("Arial", 11),
            padx=15,
            pady=8
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            button_frame,
            text="Clear",
            command=self.clear_fields,
            bg="gray",
            fg="white",
            font=("Arial", 11),
            padx=15,
            pady=8
        ).pack(side=tk.LEFT, padx=5)
        
        # ===== TABLE FRAME =====
        table_frame = tk.LabelFrame(
            self.root,
            text="Student Records",
            font=("Arial", 12, "bold"),
            padx=10,
            pady=10
        )
        table_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create Treeview (table)
        columns = ("Name", "Roll Number", "Email", "Phone", "Grade")
        self.tree = ttk.Treeview(table_frame, columns=columns, height=15)
        
        # Define column headings
        self.tree.column("#0", width=0, stretch=tk.NO)
        self.tree.column("Name", anchor=tk.W, width=150)
        self.tree.column("Roll Number", anchor=tk.CENTER, width=100)
        self.tree.column("Email", anchor=tk.W, width=180)
        self.tree.column("Phone", anchor=tk.CENTER, width=100)
        self.tree.column("Grade", anchor=tk.CENTER, width=80)
        
        # Create headings
        self.tree.heading("#0", text="", anchor=tk.W)
        self.tree.heading("Name", text="Name", anchor=tk.W)
        self.tree.heading("Roll Number", text="Roll Number", anchor=tk.CENTER)
        self.tree.heading("Email", text="Email", anchor=tk.W)
        self.tree.heading("Phone", text="Phone", anchor=tk.CENTER)
        self.tree.heading("Grade", text="Grade", anchor=tk.CENTER)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Bind row selection
        self.tree.bind("<<TreeviewSelect>>", self.on_row_select)
    
    def add_student(self):
        """Add new student"""
        name = self.name_entry.get().strip()
        roll = self.roll_entry.get().strip()
        email = self.email_entry.get().strip()
        phone = self.phone_entry.get().strip()
        grade = self.grade_var.get()
        
        # Validation
        if not all([name, roll, email, phone]):
            messagebox.showerror("Error", "Please fill all fields!")
            return
        
        # Check if roll number already exists
        if any(s["roll"] == roll for s in self.students):
            messagebox.showerror("Error", "Roll number already exists!")
            return
        
        # Add student
        student = {
            "name": name,
            "roll": roll,
            "email": email,
            "phone": phone,
            "grade": grade
        }
        
        self.students.append(student)
        self.save_data()
        self.refresh_table()
        self.clear_fields()
        messagebox.showinfo("Success", "Student added successfully!")
    
    def update_student(self):
        """Update selected student"""
        selected = self.tree.selection()
        
        if not selected:
            messagebox.showerror("Error", "Please select a student to update!")
            return
        
        name = self.name_entry.get().strip()
        roll = self.roll_entry.get().strip()
        email = self.email_entry.get().strip()
        phone = self.phone_entry.get().strip()
        grade = self.grade_var.get()
        
        if not all([name, roll, email, phone]):
            messagebox.showerror("Error", "Please fill all fields!")
            return
        
        # Update student
        item_id = selected[0]
        index = int(item_id) - 1
        
        self.students[index] = {
            "name": name,
            "roll": roll,
            "email": email,
            "phone": phone,
            "grade": grade
        }
        
        self.save_data()
        self.refresh_table()
        self.clear_fields()
        messagebox.showinfo("Success", "Student updated successfully!")
    
    def delete_student(self):
        """Delete selected student"""
        selected = self.tree.selection()
        
        if not selected:
            messagebox.showerror("Error", "Please select a student to delete!")
            return
        
        confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete this student?")
        
        if confirm:
            item_id = selected[0]
            index = int(item_id) - 1
            del self.students[index]
            
            self.save_data()
            self.refresh_table()
            self.clear_fields()
            messagebox.showinfo("Success", "Student deleted successfully!")
    
    def clear_fields(self):
        """Clear all input fields"""
        self.name_entry.delete(0, tk.END)
        self.roll_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.grade_var.set("A")
        self.tree.selection_remove(self.tree.selection())
    
    def on_row_select(self, event):
        """Handle row selection"""
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
            
            self.grade_var.set(student["grade"])
    
    def refresh_table(self):
        """Refresh the table with data"""
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Add students to table
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
                    student["grade"]
                )
            )
    
    def save_data(self):
        """Save students to JSON file"""
        with open(self.data_file, 'w') as f:
            json.dump(self.students, f, indent=4)
    
    def load_data(self):
        """Load students from JSON file"""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                return json.load(f)
        return []


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentCRUDApp(root)
    root.mainloop()
```

---

## Key Takeaways

1. **Widgets**: Label, Button, Entry, Text, Frame, Listbox, Checkbutton, Radiobutton, OptionMenu
2. **Layout Managers**: Pack, Grid, Place (Grid is best for forms)
3. **Events**: Bind, Command, Lambda for passing parameters
4. **Data Persistence**: JSON for simple applications
5. **Validation**: Always validate user input before processing
6. **OOP**: Use classes to organize complex applications

---

## Practice Exercises

1. Create a simple calculator with buttons for operations
2. Build a to-do list app with add/remove/mark complete features
3. Create a simple login form with validation
4. Build an expense tracker with monthly totals
5. Create a quiz application with scoring

---

## Resources

- [Tkinter Official Documentation](https://docs.python.org/3/library/tkinter.html)
- [Tkinter Tutorial Videos](https://www.youtube.com/results?search_query=tkinter+tutorial)
- [Real Python - Tkinter Guide](https://realpython.com/tkinter-tutorial/)

Happy coding! 🚀

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import sqlite3
from datetime import datetime
import os

class StudentManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System - CRUD Application")
        self.root.geometry("1400x900")
        self.root.configure(bg='#f8f9fa')
        self.root.state('zoomed') if os.name == 'nt' else self.root.attributes('-zoomed', True)
        
        # Configure style
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Enhanced color scheme
        self.colors = {
            'primary': '#2c3e50',
            'secondary': '#34495e',
            'success': '#27ae60',
            'danger': '#e74c3c',
            'warning': '#f39c12',
            'info': '#3498db',
            'light': '#ecf0f1',
            'dark': '#2c3e50',
            'white': '#ffffff',
            'muted': '#6c757d',
            'background': '#f8f9fa',
            'card_shadow': '#dee2e6'
        }
        
        # Configure custom styles
        self.configure_styles()
        
        # Initialize database
        self.init_database()
        
        # Create GUI
        self.create_widgets()
        
        # Load data
        self.load_students()
    
    def configure_styles(self):
        """Configure enhanced custom styles"""
        # Configure button styles with hover effects
        self.style.configure('Primary.TButton',
                           background=self.colors['primary'],
                           foreground='white',
                           font=('Segoe UI', 10, 'bold'),
                           padding=(15, 8),
                           relief='flat')
        
        self.style.map('Primary.TButton',
                      background=[('active', '#34495e')])
        
        self.style.configure('Success.TButton',
                           background=self.colors['success'],
                           foreground='white',
                           font=('Segoe UI', 10, 'bold'),
                           padding=(15, 8),
                           relief='flat')
        
        self.style.map('Success.TButton',
                      background=[('active', '#2ecc71')])
        
        self.style.configure('Danger.TButton',
                           background=self.colors['danger'],
                           foreground='white',
                           font=('Segoe UI', 10, 'bold'),
                           padding=(15, 8),
                           relief='flat')
        
        self.style.map('Danger.TButton',
                      background=[('active', '#c0392b')])
        
        self.style.configure('Warning.TButton',
                           background=self.colors['warning'],
                           foreground='white',
                           font=('Segoe UI', 10, 'bold'),
                           padding=(15, 8),
                           relief='flat')
        
        self.style.map('Warning.TButton',
                      background=[('active', '#e67e22')])
        
        self.style.configure('Info.TButton',
                           background=self.colors['info'],
                           foreground='white',
                           font=('Segoe UI', 10, 'bold'),
                           padding=(15, 8),
                           relief='flat')
        
        # Enhanced frame styles
        self.style.configure('Card.TFrame',
                           background=self.colors['white'],
                           relief='solid',
                           borderwidth=1)
        
        self.style.configure('Shadow.TFrame',
                           background=self.colors['card_shadow'],
                           relief='flat')
        
        # Enhanced label styles
        self.style.configure('Title.TLabel',
                           background=self.colors['background'],
                           font=('Segoe UI', 24, 'bold'),
                           foreground=self.colors['primary'])
        
        self.style.configure('Heading.TLabel',
                           background=self.colors['white'],
                           font=('Segoe UI', 16, 'bold'),
                           foreground=self.colors['primary'])
        
        self.style.configure('Field.TLabel',
                           background=self.colors['white'],
                           font=('Segoe UI', 11),
                           foreground=self.colors['secondary'])
        
        self.style.configure('Stats.TLabel',
                           background=self.colors['white'],
                           font=('Segoe UI', 12, 'bold'))
        
        # Enhanced entry styles
        self.style.configure('Modern.TEntry',
                           fieldbackground='white',
                           borderwidth=2,
                           relief='solid',
                           font=('Segoe UI', 11))
        
        # Enhanced combobox styles
        self.style.configure('Modern.TCombobox',
                           fieldbackground='white',
                           borderwidth=2,
                           relief='solid',
                           font=('Segoe UI', 11))
        
        # Enhanced checkbutton styles
        self.style.configure('Modern.TCheckbutton',
                           background=self.colors['white'],
                           font=('Segoe UI', 11),
                           focuscolor='none')
        
        # Enhanced radiobutton styles
        self.style.configure('Modern.TRadiobutton',
                           background=self.colors['white'],
                           font=('Segoe UI', 11),
                           focuscolor='none')
        
        # Enhanced treeview styles
        self.style.configure('Treeview',
                           background='white',
                           foreground=self.colors['dark'],
                           rowheight=30,
                           fieldbackground='white',
                           font=('Segoe UI', 10))
        
        self.style.configure('Treeview.Heading',
                           background=self.colors['primary'],
                           foreground='white',
                           font=('Segoe UI', 11, 'bold'))
        
        self.style.map('Treeview',
                      background=[('selected', self.colors['info']),
                                ('focus', self.colors['light'])])
    
    def init_database(self):
        """Initialize SQLite database and create table"""
        try:
            self.conn = sqlite3.connect('students.db')
            self.cursor = self.conn.cursor()
            
            # Create students table
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    phone TEXT,
                    age INTEGER,
                    gender TEXT,
                    course TEXT,
                    semester INTEGER,
                    is_active INTEGER DEFAULT 1,
                    has_scholarship INTEGER DEFAULT 0,
                    enrollment_date TEXT,
                    created_at TEXT DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            self.conn.commit()
            
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error connecting to database: {e}")
    
    def create_shadow_frame(self, parent, **kwargs):
        """Create a frame with shadow effect"""
        shadow = ttk.Frame(parent, style='Shadow.TFrame')
        main_frame = ttk.Frame(shadow, style='Card.TFrame', **kwargs)
        main_frame.pack(fill='both', expand=True, padx=2, pady=2)
        return shadow, main_frame
    
    def create_widgets(self):
        """Create and arrange GUI widgets with enhanced styling"""
        # Main container with padding
        main_frame = ttk.Frame(self.root, padding="30")
        main_frame.pack(fill='both', expand=True)
        
        # Title with modern styling
        title_frame = ttk.Frame(main_frame)
        title_frame.pack(fill='x', pady=(0, 30))
        
        title_label = ttk.Label(title_frame, text="🎓 Student Management System", style='Title.TLabel')
        title_label.pack()
        
        subtitle_label = ttk.Label(title_frame, text="Comprehensive CRUD Application for Academic Management",
                                 font=('Segoe UI', 12), foreground=self.colors['muted'],
                                 background=self.colors['background'])
        subtitle_label.pack(pady=(5, 0))
        
        # Main content area
        content_frame = ttk.Frame(main_frame)
        content_frame.pack(fill='both', expand=True)
        
        # Left panel - Form
        self.create_form_panel(content_frame)
        
        # Right panel - List and controls
        self.create_list_panel(content_frame)
        
        # Bottom panel - Statistics
        self.create_stats_panel(main_frame)
    
    def create_form_panel(self, parent):
        """Create enhanced form panel"""
        shadow, form_frame = self.create_shadow_frame(parent, padding="25")
        shadow.pack(side='left', fill='y', padx=(0, 15), pady=10)
        
        # Form title
        title_frame = ttk.Frame(form_frame, style='Card.TFrame')
        title_frame.pack(fill='x', pady=(0, 20))
        
        ttk.Label(title_frame, text="📝 Student Information", style='Heading.TLabel').pack()
        ttk.Frame(title_frame, height=3, style='Card.TFrame').pack(fill='x', pady=5)  # Separator line
        
        # Variables
        self.name_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.age_var = tk.StringVar()
        self.gender_var = tk.StringVar(value="Male")
        self.course_var = tk.StringVar(value="Computer Science")
        self.semester_var = tk.StringVar()
        self.is_active_var = tk.BooleanVar(value=True)
        self.has_scholarship_var = tk.BooleanVar()
        
        # Scrollable form
        canvas = tk.Canvas(form_frame, bg='white', highlightthickness=0)
        scrollbar = ttk.Scrollbar(form_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas, style='Card.TFrame')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Form fields with enhanced styling
        row = 0
        
        # Name field
        self.create_form_field(scrollable_frame, "👤 Full Name:", self.name_var, row)
        row += 1
        
        # Email field
        self.create_form_field(scrollable_frame, "📧 Email Address:", self.email_var, row)
        row += 1
        
        # Phone field
        self.create_form_field(scrollable_frame, "📱 Phone Number:", self.phone_var, row)
        row += 1
        
        # Age field
        self.create_form_field(scrollable_frame, "🎂 Age:", self.age_var, row)
        row += 1
        
        # Gender (Enhanced Radio buttons)
        gender_frame = ttk.Frame(scrollable_frame, style='Card.TFrame', padding="10")
        gender_frame.grid(row=row, column=0, columnspan=2, sticky='ew', pady=10)
        
        ttk.Label(gender_frame, text="⚧ Gender:", style='Field.TLabel').pack(anchor='w')
        
        radio_container = ttk.Frame(gender_frame, style='Card.TFrame')
        radio_container.pack(fill='x', pady=(5, 0))
        
        for i, (text, value) in enumerate([("Male", "Male"), ("Female", "Female"), ("Other", "Other")]):
            radio = ttk.Radiobutton(radio_container, text=text, variable=self.gender_var, 
                                  value=value, style='Modern.TRadiobutton')
            radio.pack(side='left', padx=(0, 20))
        row += 1
        
        # Course field
        course_frame = ttk.Frame(scrollable_frame, style='Card.TFrame', padding="10")
        course_frame.grid(row=row, column=0, columnspan=2, sticky='ew', pady=10)
        
        ttk.Label(course_frame, text="📚 Course:", style='Field.TLabel').pack(anchor='w')
        course_combo = ttk.Combobox(course_frame, textvariable=self.course_var, style='Modern.TCombobox')
        course_combo['values'] = ('Computer Science', 'Information Technology', 'Software Engineering', 
                                 'Data Science', 'Cybersecurity', 'Web Development', 'Artificial Intelligence')
        course_combo.pack(fill='x', pady=(5, 0))
        row += 1
        
        # Semester field
        semester_frame = ttk.Frame(scrollable_frame, style='Card.TFrame', padding="10")
        semester_frame.grid(row=row, column=0, columnspan=2, sticky='ew', pady=10)
        
        ttk.Label(semester_frame, text="📅 Semester:", style='Field.TLabel').pack(anchor='w')
        semester_combo = ttk.Combobox(semester_frame, textvariable=self.semester_var, style='Modern.TCombobox')
        semester_combo['values'] = tuple(range(1, 9))  # 1-8 semesters
        semester_combo.pack(fill='x', pady=(5, 0))
        row += 1
        
        # Enhanced Checkboxes
        checkbox_frame = ttk.Frame(scrollable_frame, style='Card.TFrame', padding="10")
        checkbox_frame.grid(row=row, column=0, columnspan=2, sticky='ew', pady=15)
        
        ttk.Label(checkbox_frame, text="⚙️ Settings:", style='Field.TLabel').pack(anchor='w')
        
        check_container = ttk.Frame(checkbox_frame, style='Card.TFrame')
        check_container.pack(fill='x', pady=(5, 0))
        
        active_check = ttk.Checkbutton(check_container, text="✅ Active Student", 
                                     variable=self.is_active_var, style='Modern.TCheckbutton')
        active_check.pack(anchor='w', pady=2)
        
        scholarship_check = ttk.Checkbutton(check_container, text="🏆 Has Scholarship", 
                                          variable=self.has_scholarship_var, style='Modern.TCheckbutton')
        scholarship_check.pack(anchor='w', pady=2)
        row += 1
        
        # Enhanced Buttons
        button_frame = ttk.Frame(scrollable_frame, style='Card.TFrame', padding="15")
        button_frame.grid(row=row, column=0, columnspan=2, sticky='ew', pady=20)
        
        # Button grid layout
        btn_grid = ttk.Frame(button_frame, style='Card.TFrame')
        btn_grid.pack(fill='x')
        
        ttk.Button(btn_grid, text="➕ Add Student", command=self.add_student, 
                  style='Success.TButton').grid(row=0, column=0, padx=5, pady=5, sticky='ew')
        ttk.Button(btn_grid, text="✏️ Update", command=self.update_student, 
                  style='Primary.TButton').grid(row=0, column=1, padx=5, pady=5, sticky='ew')
        ttk.Button(btn_grid, text="🗑️ Delete", command=self.delete_student, 
                  style='Danger.TButton').grid(row=1, column=0, padx=5, pady=5, sticky='ew')
        ttk.Button(btn_grid, text="🔄 Clear", command=self.clear_form, 
                  style='Warning.TButton').grid(row=1, column=1, padx=5, pady=5, sticky='ew')
        
        btn_grid.columnconfigure(0, weight=1)
        btn_grid.columnconfigure(1, weight=1)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        scrollable_frame.columnconfigure(0, weight=1)
        scrollable_frame.columnconfigure(1, weight=1)
    
    def create_form_field(self, parent, label_text, variable, row):
        """Create a styled form field"""
        field_frame = ttk.Frame(parent, style='Card.TFrame', padding="10")
        field_frame.grid(row=row, column=0, columnspan=2, sticky='ew', pady=10)
        
        ttk.Label(field_frame, text=label_text, style='Field.TLabel').pack(anchor='w')
        entry = ttk.Entry(field_frame, textvariable=variable, style='Modern.TEntry', font=('Segoe UI', 11))
        entry.pack(fill='x', pady=(5, 0))
        
        return entry
    
    def create_list_panel(self, parent):
        """Create enhanced student list panel"""
        shadow, list_frame = self.create_shadow_frame(parent, padding="25")
        shadow.pack(side='right', fill='both', expand=True, pady=10)
        
        # Panel title
        title_frame = ttk.Frame(list_frame, style='Card.TFrame')
        title_frame.pack(fill='x', pady=(0, 20))
        
        ttk.Label(title_frame, text="👥 Student Directory", style='Heading.TLabel').pack()
        ttk.Frame(title_frame, height=3, style='Card.TFrame').pack(fill='x', pady=5)
        
        # Enhanced search frame
        search_frame = ttk.Frame(list_frame, style='Card.TFrame', padding="15")
        search_frame.pack(fill='x', pady=(0, 15))
        
        search_left = ttk.Frame(search_frame, style='Card.TFrame')
        search_left.pack(side='left', fill='x', expand=True)
        
        ttk.Label(search_left, text="🔍 Search:", style='Field.TLabel').pack(side='left')
        self.search_var = tk.StringVar()
        search_entry = ttk.Entry(search_left, textvariable=self.search_var, 
                               style='Modern.TEntry', font=('Segoe UI', 11), width=25)
        search_entry.pack(side='left', padx=(10, 0), fill='x', expand=True)
        search_entry.bind('<KeyRelease>', self.search_students)
        
        search_right = ttk.Frame(search_frame, style='Card.TFrame')
        search_right.pack(side='right')
        
        ttk.Button(search_right, text="🔄 Refresh", command=self.load_students, 
                  style='Info.TButton').pack(side='left', padx=5)
        ttk.Button(search_right, text="📤 Export", command=self.export_data, 
                  style='Success.TButton').pack(side='left', padx=5)
        
        # Enhanced Treeview with modern styling
        tree_frame = ttk.Frame(list_frame, style='Card.TFrame')
        tree_frame.pack(fill='both', expand=True)
        
        # Treeview
        self.tree = ttk.Treeview(tree_frame, 
                               columns=('ID', 'Name', 'Email', 'Phone', 'Course', 'Semester', 'Status'), 
                               show='headings', height=20)
        
        # Define headings with icons
        headers = {
            'ID': ('🆔', 60),
            'Name': ('👤 Name', 150),
            'Email': ('📧 Email', 200),
            'Phone': ('📱 Phone', 120),
            'Course': ('📚 Course', 150),
            'Semester': ('📅 Sem', 80),
            'Status': ('⚡ Status', 100)
        }
        
        for col, (header, width) in headers.items():
            self.tree.heading(col, text=header)
            self.tree.column(col, width=width, anchor='center' if col in ['ID', 'Semester', 'Status'] else 'w')
        
        # Enhanced scrollbars
        v_scrollbar = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=self.tree.yview)
        h_scrollbar = ttk.Scrollbar(tree_frame, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.tree.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
        
        # Grid treeview and scrollbars
        self.tree.grid(row=0, column=0, sticky='nsew')
        v_scrollbar.grid(row=0, column=1, sticky='ns')
        h_scrollbar.grid(row=1, column=0, sticky='ew')
        
        tree_frame.grid_rowconfigure(0, weight=1)
        tree_frame.grid_columnconfigure(0, weight=1)
        
        # Bind selection event
        self.tree.bind('<<TreeviewSelect>>', self.on_select)
        
        # Add alternating row colors
        self.tree.tag_configure('oddrow', background='#f8f9fa')
        self.tree.tag_configure('evenrow', background='white')
    
    def create_stats_panel(self, parent):
        """Create enhanced statistics panel"""
        shadow, stats_frame = self.create_shadow_frame(parent, padding="20")
        shadow.pack(fill='x', pady=(20, 0))
        
        # Stats title
        title_frame = ttk.Frame(stats_frame, style='Card.TFrame')
        title_frame.pack(fill='x', pady=(0, 15))
        
        ttk.Label(title_frame, text="📊 Dashboard Statistics", style='Heading.TLabel').pack()
        
        # Stats container
        stats_container = ttk.Frame(stats_frame, style='Card.TFrame')
        stats_container.pack(fill='x')
        
        # Stats cards
        self.create_stat_card(stats_container, "👥 Total Students", "0", self.colors['primary'], 0)
        self.create_stat_card(stats_container, "✅ Active Students", "0", self.colors['success'], 1)
        self.create_stat_card(stats_container, "🏆 Scholarships", "0", self.colors['warning'], 2)
        self.create_stat_card(stats_container, "🕐 Last Updated", "Never", self.colors['info'], 3)
        
        for i in range(4):
            stats_container.columnconfigure(i, weight=1)
    
    def create_stat_card(self, parent, title, value, color, column):
        """Create individual stat card"""
        card_frame = ttk.Frame(parent, style='Card.TFrame', padding="15")
        card_frame.grid(row=0, column=column, padx=10, sticky='ew')
        
        title_label = ttk.Label(card_frame, text=title, font=('Segoe UI', 10), 
                              foreground=self.colors['muted'], background='white')
        title_label.pack()
        
        value_label = ttk.Label(card_frame, text=value, font=('Segoe UI', 16, 'bold'), 
                              foreground=color, background='white')
        value_label.pack()
        
        # Store reference for updates
        if 'Total' in title:
            self.total_students_label = value_label
        elif 'Active' in title:
            self.active_students_label = value_label
        elif 'Scholarships' in title:
            self.scholarship_students_label = value_label
        elif 'Updated' in title:
            self.last_updated_label = value_label
    
    def add_student(self):
        """Add new student to database"""
        if not self.validate_form():
            return
        
        try:
            self.cursor.execute('''
                INSERT INTO students (name, email, phone, age, gender, course, semester, 
                                    is_active, has_scholarship, enrollment_date)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                self.name_var.get().strip(),
                self.email_var.get().strip(),
                self.phone_var.get().strip(),
                int(self.age_var.get()),
                self.gender_var.get(),
                self.course_var.get(),
                int(self.semester_var.get()),
                1 if self.is_active_var.get() else 0,
                1 if self.has_scholarship_var.get() else 0,
                datetime.now().strftime("%Y-%m-%d")
            ))
            
            self.conn.commit()
            messagebox.showinfo("✅ Success", "Student added successfully!")
            self.clear_form()
            self.load_students()
            
        except sqlite3.IntegrityError:
            messagebox.showerror("❌ Error", "Email already exists!")
        except ValueError:
            messagebox.showerror("❌ Error", "Age and Semester must be numbers!")
        except sqlite3.Error as e:
            messagebox.showerror("❌ Database Error", f"Error adding student: {e}")
    
    def update_student(self):
        """Update selected student"""
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("⚠️ Warning", "Please select a student to update!")
            return
        
        if not self.validate_form():
            return
        
        try:
            item = self.tree.item(selected[0])
            student_id = item['values'][0]
            
            self.cursor.execute('''
                UPDATE students 
                SET name=?, email=?, phone=?, age=?, gender=?, course=?, semester=?, 
                    is_active=?, has_scholarship=?
                WHERE id=?
            ''', (
                self.name_var.get().strip(),
                self.email_var.get().strip(),
                self.phone_var.get().strip(),
                int(self.age_var.get()),
                self.gender_var.get(),
                self.course_var.get(),
                int(self.semester_var.get()),
                1 if self.is_active_var.get() else 0,
                1 if self.has_scholarship_var.get() else 0,
                student_id
            ))
            
            self.conn.commit()
            messagebox.showinfo("✅ Success", "Student updated successfully!")
            self.clear_form()
            self.load_students()
            
        except ValueError:
            messagebox.showerror("❌ Error", "Age and Semester must be numbers!")
        except sqlite3.Error as e:
            messagebox.showerror("❌ Database Error", f"Error updating student: {e}")
    
    def delete_student(self):
        """Delete selected student"""
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("⚠️ Warning", "Please select a student to delete!")
            return
        
        item = self.tree.item(selected[0])
        student_name = item['values'][1]
        
        result = messagebox.askyesno("🗑️ Confirm Delete", 
                                   f"Are you sure you want to delete '{student_name}'?\n\nThis action cannot be undone.")
        if result:
            try:
                student_id = item['values'][0]
                
                self.cursor.execute('DELETE FROM students WHERE id=?', (student_id,))
                self.conn.commit()
                
                messagebox.showinfo("✅ Success", "Student deleted successfully!")
                self.clear_form()
                self.load_students()
                
            except sqlite3.Error as e:
                messagebox.showerror("❌ Database Error", f"Error deleting student: {e}")
    
    def load_students(self):
        """Load all students into treeview with enhanced display"""
        # Clear existing data
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        try:
            self.cursor.execute('SELECT * FROM students ORDER BY name')
            students = self.cursor.fetchall()
            
            for i, student in enumerate(students):
                status = "🟢 Active" if student[8] else "🔴 Inactive"
                scholarship = "🏆" if student[9] else ""
                
                # Apply alternating row colors
                tag = 'evenrow' if i % 2 == 0 else 'oddrow'
                
                self.tree.insert('', 'end', values=(
                    student[0],  # ID
                    f"{student[1]} {scholarship}",  # Name with scholarship indicator
                    student[2],  # Email
                    student[3] or "N/A",  # Phone
                    student[6],  # Course
                    f"Sem {student[7]}",  # Semester
                    status       # Status
                ), tags=(tag,))
                
        except sqlite3.Error as e:
            messagebox.showerror("❌ Database Error", f"Error searching students: {e}")
    
    def on_select(self, event):
        """Handle treeview selection with improved data loading"""
        selected = self.tree.selection()
        if selected:
            try:
                item = self.tree.item(selected[0])
                student_id = item['values'][0]
                
                self.cursor.execute('SELECT * FROM students WHERE id=?', (student_id,))
                student = self.cursor.fetchone()
                
                if student:
                    # Populate form with selected student data
                    self.name_var.set(student[1])
                    self.email_var.set(student[2])
                    self.phone_var.set(student[3] or "")
                    self.age_var.set(str(student[4]))
                    self.gender_var.set(student[5])
                    self.course_var.set(student[6])
                    self.semester_var.set(str(student[7]))
                    self.is_active_var.set(bool(student[8]))
                    self.has_scholarship_var.set(bool(student[9]))
                    
            except sqlite3.Error as e:
                messagebox.showerror("❌ Database Error", f"Error loading student details: {e}")
    
    def clear_form(self):
        """Clear all form fields with improved reset"""
        self.name_var.set("")
        self.email_var.set("")
        self.phone_var.set("")
        self.age_var.set("")
        self.gender_var.set("Male")
        self.course_var.set("Computer Science")
        self.semester_var.set("")
        self.is_active_var.set(True)
        self.has_scholarship_var.set(False)
        
        # Clear treeview selection
        for item in self.tree.selection():
            self.tree.selection_remove(item)
    
    def validate_form(self):
        """Enhanced form validation with better error messages"""
        # Name validation
        if not self.name_var.get().strip():
            messagebox.showerror("❌ Validation Error", "Name is required!")
            return False
        
        if len(self.name_var.get().strip()) < 2:
            messagebox.showerror("❌ Validation Error", "Name must be at least 2 characters long!")
            return False
        
        # Email validation
        if not self.email_var.get().strip():
            messagebox.showerror("❌ Validation Error", "Email is required!")
            return False
        
        email = self.email_var.get().strip()
        if '@' not in email or '.' not in email.split('@')[1]:
            messagebox.showerror("❌ Validation Error", "Please enter a valid email address!")
            return False
        
        # Phone validation (optional but if provided, should be valid)
        phone = self.phone_var.get().strip()
        if phone and (len(phone) < 10 or not phone.replace('+', '').replace('-', '').replace(' ', '').isdigit()):
            messagebox.showerror("❌ Validation Error", "Please enter a valid phone number!")
            return False
        
        # Age validation
        try:
            age = int(self.age_var.get())
            if age < 16 or age > 100:
                messagebox.showerror("❌ Validation Error", "Age must be between 16 and 100!")
                return False
        except ValueError:
            messagebox.showerror("❌ Validation Error", "Age must be a valid number!")
            return False
        
        # Semester validation
        try:
            semester = int(self.semester_var.get())
            if semester < 1 or semester > 8:
                messagebox.showerror("❌ Validation Error", "Semester must be between 1 and 8!")
                return False
        except ValueError:
            messagebox.showerror("❌ Validation Error", "Semester must be a valid number!")
            return False
        
        return True
    
    def update_statistics(self):
        """Update statistics panel with enhanced display"""
        try:
            # Total students
            self.cursor.execute('SELECT COUNT(*) FROM students')
            total = self.cursor.fetchone()[0]
            
            # Active students
            self.cursor.execute('SELECT COUNT(*) FROM students WHERE is_active = 1')
            active = self.cursor.fetchone()[0]
            
            # Students with scholarships
            self.cursor.execute('SELECT COUNT(*) FROM students WHERE has_scholarship = 1')
            scholarships = self.cursor.fetchone()[0]
            
            # Update labels with enhanced formatting
            self.total_students_label.config(text=str(total))
            self.active_students_label.config(text=str(active))
            self.scholarship_students_label.config(text=str(scholarships))
            self.last_updated_label.config(text=datetime.now().strftime('%H:%M:%S'))
            
        except sqlite3.Error as e:
            messagebox.showerror("❌ Database Error", f"Error updating statistics: {e}")
    
    def export_data(self):
        """Export student data to CSV with enhanced formatting"""
        try:
            filename = filedialog.asksaveasfilename(
                defaultextension=".csv",
                filetypes=[("CSV files", "*.csv"), ("Text files", "*.txt"), ("All files", "*.*")],
                title="Export Student Data"
            )
            
            if filename:
                self.cursor.execute('SELECT * FROM students ORDER BY name')
                students = self.cursor.fetchall()
                
                with open(filename, 'w', newline='', encoding='utf-8') as file:
                    # Enhanced CSV header
                    file.write("ID,Name,Email,Phone,Age,Gender,Course,Semester,Active,Scholarship,Enrollment Date,Created At\n")
                    for student in students:
                        # Format the data properly
                        row = [
                            str(student[0]),  # ID
                            f'"{student[1]}"',  # Name (quoted)
                            f'"{student[2]}"',  # Email (quoted)
                            f'"{student[3] or ""}"',  # Phone (quoted, handle None)
                            str(student[4]),  # Age
                            f'"{student[5]}"',  # Gender (quoted)
                            f'"{student[6]}"',  # Course (quoted)
                            str(student[7]),  # Semester
                            "Yes" if student[8] else "No",  # Active
                            "Yes" if student[9] else "No",  # Scholarship
                            f'"{student[10] or ""}"',  # Enrollment Date (quoted)
                            f'"{student[11] or ""}"'   # Created At (quoted)
                        ]
                        file.write(','.join(row) + '\n')
                
                messagebox.showinfo("✅ Export Complete", 
                                  f"Successfully exported {len(students)} student records to:\n{filename}")
                
        except Exception as e:
            messagebox.showerror("❌ Export Error", f"Error exporting data: {e}")
    
    def create_backup(self):
        """Create database backup"""
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_filename = f"students_backup_{timestamp}.db"
            
            # Create backup
            backup_conn = sqlite3.connect(backup_filename)
            self.conn.backup(backup_conn)
            backup_conn.close()
            
            messagebox.showinfo("✅ Backup Complete", f"Database backed up to: {backup_filename}")
            
        except Exception as e:
            messagebox.showerror("❌ Backup Error", f"Error creating backup: {e}")
    
    def show_about(self):
        """Show about dialog"""
        about_text = """
        🎓 Student Management System
        
        Version: 2.0
        
        A comprehensive CRUD application for managing student records.
        
        Features:
        ✅ Add, Edit, Update, Delete students
        🔍 Search and filter functionality
        📊 Real-time statistics
        📤 Export to CSV
        🎨 Modern, responsive UI
        
        Developed for Python Programming Course
        Bachelor's Level Academic Project
        
        Technologies Used:
        • Python 3.x
        • Tkinter (GUI)
        • SQLite3 (Database)
        • Object-Oriented Programming
        """
        messagebox.showinfo("About Student Management System", about_text)
    
    def on_closing(self):
        """Handle application closing"""
        if messagebox.askokcancel("Quit", "Do you want to quit the application?"):
            try:
                self.conn.close()
            except:
                pass
            self.root.destroy()
    
    def __del__(self):
        """Cleanup database connection"""
        try:
            if hasattr(self, 'conn'):
                self.conn.close()
        except:
            pass
    
    def search_students(self, event=None):
        """Search students with enhanced filtering"""
        search_term = self.search_var.get().strip().lower()
        
        # Clear existing data
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        try:
            if search_term:
                self.cursor.execute('''
                    SELECT * FROM students 
                    WHERE LOWER(name) LIKE ? 
                       OR LOWER(email) LIKE ? 
                       OR LOWER(course) LIKE ? 
                       OR phone LIKE ?
                    ORDER BY name
                ''', (f'%{search_term}%', f'%{search_term}%', f'%{search_term}%', f'%{search_term}%'))
            else:
                self.cursor.execute('SELECT * FROM students ORDER BY name')
            
            students = self.cursor.fetchall()
            
            for i, student in enumerate(students):
                status = "🟢 Active" if student[8] else "🔴 Inactive"
                scholarship = "🏆" if student[9] else ""
                
                tag = 'evenrow' if i % 2 == 0 else 'oddrow'
                
                self.tree.insert('', 'end', values=(
                    student[0],  # ID
                    f"{student[1]} {scholarship}",  # Name with scholarship indicator
                    student[2],  # Email
                    student[3] or "N/A",  # Phone
                    student[6],  # Course
                    f"Sem {student[7]}",  # Semester
                    status
                ), tags=(tag,))
            
            # Update stats when search results are shown
            self.update_statistics()
        
        except sqlite3.Error as e:
            messagebox.showerror("❌ Database Error", f"Error searching students: {e}")


def main():
    """Main application entry point"""
    root = tk.Tk()
    
    # Set window icon (if available)
    try:
        root.iconbitmap('student_icon.ico')
    except:
        pass  # Icon file not found, continue without it
    
    # Initialize application
    app = StudentManagementSystem(root)
    
    # Handle window closing
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    
    # Add menu bar
    menubar = tk.Menu(root)
    root.config(menu=menubar)
    
    # File menu
    file_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Export Data", command=app.export_data)
    file_menu.add_command(label="Create Backup", command=app.create_backup)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=app.on_closing)
    
    # Help menu
    help_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="About", command=app.show_about)
    
    # Start application
    root.mainloop()

if __name__ == "__main__":
    main()
    
    
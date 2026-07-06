# ============================================
# TKINTER GRID LAYOUT - Examples
# ============================================

import tkinter as tk
from tkinter import messagebox

# ============================================
# Example 1: Basic Grid Layout
# ============================================
def example_1_basic_grid():
    """Simple 3x3 grid layout"""
    root = tk.Tk()
    root.title("Basic Grid Layout")
    root.geometry("400x300")
    
    # Create 3x3 grid of labels
    for row in range(3):
        for col in range(3):
            label = tk.Label(
                root,
                text=f"Row {row}, Col {col}",
                font=("Arial", 10),
                bg="lightblue",
                relief=tk.RAISED,
                borderwidth=1
            )
            label.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    
    root.mainloop()


# ============================================
# Example 2: Login Form with Grid
# ============================================
def example_2_login_form():
    """Professional login form using grid"""
    root = tk.Tk()
    root.title("Login Form")
    root.geometry("400x250")
    
    # Title
    title = tk.Label(
        root,
        text="User Login",
        font=("Arial", 16, "bold"),
        bg="darkblue",
        fg="white"
    )
    title.grid(row=0, column=0, columnspan=2, sticky="ew", padx=0, pady=20)
    
    # Username
    tk.Label(root, text="Username:", font=("Arial", 11)).grid(
        row=1, column=0, sticky="w", padx=20, pady=10
    )
    username_entry = tk.Entry(root, font=("Arial", 11), width=25)
    username_entry.grid(row=1, column=1, padx=20, pady=10)
    
    # Password
    tk.Label(root, text="Password:", font=("Arial", 11)).grid(
        row=2, column=0, sticky="w", padx=20, pady=10
    )
    password_entry = tk.Entry(root, font=("Arial", 11), width=25, show="*")
    password_entry.grid(row=2, column=1, padx=20, pady=10)
    
    # Remember me checkbox
    remember_var = tk.BooleanVar()
    remember = tk.Checkbutton(
        root,
        text="Remember me",
        variable=remember_var
    )
    remember.grid(row=3, column=0, columnspan=2, sticky="w", padx=20, pady=10)
    
    # Login button
    def login():
        username = username_entry.get()
        password = password_entry.get()
        if username and password:
            messagebox.showinfo("Success", f"Welcome {username}!")
        else:
            messagebox.showerror("Error", "Please fill all fields!")
    
    login_btn = tk.Button(
        root,
        text="Login",
        command=login,
        bg="green",
        fg="white",
        font=("Arial", 11),
        width=20
    )
    login_btn.grid(row=4, column=0, columnspan=2, pady=20)
    
    root.mainloop()


# ============================================
# Example 3: Registration Form
# ============================================
def example_3_registration_form():
    """Detailed registration form with multiple fields"""
    root = tk.Tk()
    root.title("Registration Form")
    root.geometry("550x500")
    
    # Title
    title = tk.Label(
        root,
        text="User Registration",
        font=("Arial", 16, "bold"),
        bg="navy",
        fg="white"
    )
    title.grid(row=0, column=0, columnspan=2, sticky="ew", padx=0, pady=15)
    
    # First Name
    tk.Label(root, text="First Name:", font=("Arial", 11)).grid(
        row=1, column=0, sticky="w", padx=20, pady=10
    )
    first_name = tk.Entry(root, font=("Arial", 11), width=30)
    first_name.grid(row=1, column=1, padx=20, pady=10)
    
    # Last Name
    tk.Label(root, text="Last Name:", font=("Arial", 11)).grid(
        row=2, column=0, sticky="w", padx=20, pady=10
    )
    last_name = tk.Entry(root, font=("Arial", 11), width=30)
    last_name.grid(row=2, column=1, padx=20, pady=10)
    
    # Email
    tk.Label(root, text="Email:", font=("Arial", 11)).grid(
        row=3, column=0, sticky="w", padx=20, pady=10
    )
    email = tk.Entry(root, font=("Arial", 11), width=30)
    email.grid(row=3, column=1, padx=20, pady=10)
    
    # Phone
    tk.Label(root, text="Phone:", font=("Arial", 11)).grid(
        row=4, column=0, sticky="w", padx=20, pady=10
    )
    phone = tk.Entry(root, font=("Arial", 11), width=30)
    phone.grid(row=4, column=1, padx=20, pady=10)
    
    # Country
    tk.Label(root, text="Country:", font=("Arial", 11)).grid(
        row=5, column=0, sticky="w", padx=20, pady=10
    )
    country_var = tk.StringVar(root)
    country_var.set("Select Country")
    countries = ["USA", "UK", "Canada", "India", "Australia", "Germany", "France"]
    country_menu = tk.OptionMenu(root, country_var, *countries)
    country_menu.grid(row=5, column=1, sticky="ew", padx=20, pady=10)
    
    # Skills (checkbuttons)
    tk.Label(root, text="Skills:", font=("Arial", 11)).grid(
        row=6, column=0, sticky="w", padx=20, pady=10
    )
    
    skills_frame = tk.Frame(root)
    skills_frame.grid(row=6, column=1, sticky="w", padx=20, pady=10)
    
    python_var = tk.BooleanVar()
    js_var = tk.BooleanVar()
    java_var = tk.BooleanVar()
    
    tk.Checkbutton(skills_frame, text="Python", variable=python_var).pack(anchor="w")
    tk.Checkbutton(skills_frame, text="JavaScript", variable=js_var).pack(anchor="w")
    tk.Checkbutton(skills_frame, text="Java", variable=java_var).pack(anchor="w")
    
    # Experience
    tk.Label(root, text="Experience:", font=("Arial", 11)).grid(
        row=7, column=0, sticky="w", padx=20, pady=10
    )
    
    exp_frame = tk.Frame(root)
    exp_frame.grid(row=7, column=1, sticky="w", padx=20, pady=10)
    
    exp_var = tk.StringVar(value="entry")
    
    tk.Radiobutton(exp_frame, text="Entry Level", variable=exp_var, value="entry").pack(anchor="w")
    tk.Radiobutton(exp_frame, text="Mid Level", variable=exp_var, value="mid").pack(anchor="w")
    tk.Radiobutton(exp_frame, text="Senior", variable=exp_var, value="senior").pack(anchor="w")
    
    # Agreement
    agree_var = tk.BooleanVar()
    agree_check = tk.Checkbutton(
        root,
        text="I agree to the terms and conditions",
        variable=agree_var,
        font=("Arial", 10)
    )
    agree_check.grid(row=8, column=0, columnspan=2, sticky="w", padx=20, pady=20)
    
    # Buttons
    btn_frame = tk.Frame(root)
    btn_frame.grid(row=9, column=0, columnspan=2, sticky="ew", padx=20, pady=20)
    
    def register():
        if not all([first_name.get(), last_name.get(), email.get(), phone.get()]):
            messagebox.showerror("Error", "Please fill all fields!")
            return
        if not agree_var.get():
            messagebox.showerror("Error", "Please agree to terms!")
            return
        messagebox.showinfo("Success", f"Welcome {first_name.get()}!")
    
    tk.Button(
        btn_frame,
        text="Register",
        command=register,
        bg="green",
        fg="white",
        font=("Arial", 11),
        width=20
    ).pack(side=tk.LEFT, padx=5)
    
    tk.Button(
        btn_frame,
        text="Clear",
        command=lambda: [first_name.delete(0, tk.END), last_name.delete(0, tk.END)],
        bg="gray",
        fg="white",
        font=("Arial", 11),
        width=20
    ).pack(side=tk.LEFT, padx=5)
    
    root.mainloop()


# ============================================
# Example 4: Product Pricing Table
# ============================================
def example_4_pricing_table():
    """Grid layout for pricing comparison table"""
    root = tk.Tk()
    root.title("Pricing Table")
    root.geometry("700x400")
    
    # Title
    title = tk.Label(
        root,
        text="Pricing Plans",
        font=("Arial", 16, "bold"),
        bg="darkgreen",
        fg="white"
    )
    title.grid(row=0, column=0, columnspan=4, sticky="ew", padx=0, pady=15)
    
    # Header row
    headers = ["Feature", "Basic", "Pro", "Premium"]
    for col, header in enumerate(headers):
        label = tk.Label(
            root,
            text=header,
            font=("Arial", 11, "bold"),
            bg="lightgray",
            relief=tk.RAISED
        )
        label.grid(row=1, column=col, sticky="ew", padx=2, pady=2)
    
    # Data rows
    data = [
        ["Price", "$9.99", "$19.99", "$29.99"],
        ["Users", "1", "5", "Unlimited"],
        ["Storage", "10GB", "100GB", "1TB"],
        ["Support", "Email", "Email & Chat", "24/7 Phone"],
        ["Updates", "No", "Yes", "Yes"],
        ["API Access", "No", "Limited", "Full"],
    ]
    
    for row_idx, row_data in enumerate(data, start=2):
        for col_idx, value in enumerate(row_data):
            # Alternate row colors
            bg_color = "white" if row_idx % 2 == 0 else "lightyellow"
            
            label = tk.Label(
                root,
                text=value,
                font=("Arial", 10),
                bg=bg_color,
                relief=tk.SUNKEN,
                borderwidth=1
            )
            label.grid(row=row_idx, column=col_idx, sticky="ew", padx=2, pady=2)
    
    # Make columns equal width
    for i in range(4):
        root.grid_columnconfigure(i, weight=1)
    
    root.mainloop()


# ============================================
# Example 5: Calculator with Grid
# ============================================
def example_5_calculator():
    """Simple calculator using grid layout"""
    root = tk.Tk()
    root.title("Calculator")
    root.geometry("300x400")
    
    # Display
    display_var = tk.StringVar(value="0")
    display = tk.Entry(
        root,
        textvar=display_var,
        font=("Arial", 16),
        justify="right",
        state="readonly"
    )
    display.grid(row=0, column=0, columnspan=4, sticky="ew", padx=5, pady=10, ipady=10)
    
    # Buttons layout
    buttons = [
        ["7", "8", "9", "/"],
        ["4", "5", "6", "*"],
        ["1", "2", "3", "-"],
        ["0", ".", "=", "+"]
    ]
    
    # Create buttons
    def button_click(value):
        current = display_var.get()
        if value == "=":
            try:
                result = eval(current)
                display_var.set(result)
            except:
                display_var.set("Error")
        elif value == "C":
            display_var.set("0")
        else:
            if current == "0":
                display_var.set(value)
            else:
                display_var.set(current + value)
    
    for row_idx, row in enumerate(buttons, start=1):
        for col_idx, btn_value in enumerate(row):
            color = "lightgreen" if btn_value == "=" else "lightgray"
            
            btn = tk.Button(
                root,
                text=btn_value,
                font=("Arial", 14),
                bg=color,
                command=lambda v=btn_value: button_click(v)
            )
            btn.grid(row=row_idx, column=col_idx, sticky="nsew", padx=2, pady=2)
    
    # Clear button
    clear_btn = tk.Button(
        root,
        text="C",
        font=("Arial", 14),
        bg="red",
        fg="white",
        command=lambda: button_click("C")
    )
    clear_btn.grid(row=5, column=0, columnspan=4, sticky="nsew", padx=2, pady=2)
    
    # Make buttons equal size
    for i in range(4):
        root.grid_columnconfigure(i, weight=1)
    for i in range(6):
        root.grid_rowconfigure(i, weight=1)
    
    root.mainloop()


# ============================================
# MAIN MENU
# ============================================
def main():
    """Main menu"""
    root = tk.Tk()
    root.title("Tkinter Grid Layout Examples")
    root.geometry("500x350")
    
    # Title
    tk.Label(
        root,
        text="Grid Layout Examples",
        font=("Arial", 16, "bold"),
        bg="darkblue",
        fg="white",
        pady=20
    ).pack(fill=tk.X)
    
    # Examples
    examples = [
        ("1. Basic Grid (3x3)", example_1_basic_grid),
        ("2. Login Form", example_2_login_form),
        ("3. Registration Form", example_3_registration_form),
        ("4. Pricing Table", example_4_pricing_table),
        ("5. Calculator", example_5_calculator),
    ]
    
    # Buttons
    btn_frame = tk.Frame(root)
    btn_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)
    
    for name, func in examples:
        tk.Button(
            btn_frame,
            text=name,
            command=func,
            font=("Arial", 11),
            bg="steelblue",
            fg="white",
            padx=20,
            pady=12,
            width=30
        ).pack(pady=8)
    
    tk.Button(
        root,
        text="Exit",
        command=root.quit,
        font=("Arial", 11),
        bg="red",
        fg="white",
        padx=20,
        pady=10
    ).pack(pady=20)
    
    root.mainloop()


if __name__ == "__main__":
    main()

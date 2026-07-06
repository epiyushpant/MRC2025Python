# ============================================
# TKINTER BASICS - Runnable Examples
# ============================================

import tkinter as tk
from tkinter import messagebox

# ============================================
# Example 1: Simple Window
# ============================================
def example_1_simple_window():
    """Most basic Tkinter window"""
    root = tk.Tk()
    root.title("My First Window")
    root.geometry("400x300")
    root.config(bg="lightblue")
    
    label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 20, "bold"))
    label.pack(pady=50)
    
    root.mainloop()


# ============================================
# Example 2: Label and Button
# ============================================
def example_2_label_button():
    """Working with labels and buttons"""
    root = tk.Tk()
    root.title("Label and Button")
    root.geometry("400x200")
    
    # Label
    label = tk.Label(
        root,
        text="Press the button!",
        font=("Arial", 14),
        fg="navy",
        bg="lightyellow"
    )
    label.pack(pady=20)
    
    # Counter variable
    counter = {"value": 0}
    
    # Button click handler
    def on_button_click():
        counter["value"] += 1
        label.config(text=f"Button clicked {counter['value']} times!")
    
    # Button
    button = tk.Button(
        root,
        text="Click Me!",
        command=on_button_click,
        font=("Arial", 12),
        bg="green",
        fg="white",
        padx=20,
        pady=10
    )
    button.pack(pady=10)
    
    root.mainloop()


# ============================================
# Example 3: Text Entry
# ============================================
def example_3_text_entry():
    """Working with text input"""
    root = tk.Tk()
    root.title("Text Entry")
    root.geometry("400x250")
    
    # Label
    label = tk.Label(root, text="Enter your name:", font=("Arial", 12))
    label.pack(pady=10)
    
    # Entry widget
    entry = tk.Entry(root, font=("Arial", 12), width=30)
    entry.pack(pady=5)
    entry.insert(0, "Type here...")
    
    # Output label
    output_label = tk.Label(root, text="", font=("Arial", 11), fg="blue")
    output_label.pack(pady=10)
    
    # Submit button
    def submit():
        name = entry.get()
        if name and name != "Type here...":
            output_label.config(text=f"Hello, {name}!")
        else:
            output_label.config(text="Please enter a name!", fg="red")
    
    button = tk.Button(root, text="Submit", command=submit, bg="blue", fg="white")
    button.pack(pady=10)
    
    root.mainloop()


# ============================================
# Example 4: Multiple Widgets with Pack
# ============================================
def example_4_multiple_widgets():
    """Multiple widgets arranged with pack"""
    root = tk.Tk()
    root.title("Multiple Widgets")
    root.geometry("400x350")
    
    # Header
    header = tk.Label(
        root,
        text="Welcome!",
        font=("Arial", 18, "bold"),
        fg="white",
        bg="darkblue",
        pady=20
    )
    header.pack(fill=tk.X)
    
    # Body frame
    body = tk.Frame(root, bg="lightgray")
    body.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
    
    # Content in body
    tk.Label(
        body,
        text="This is a label",
        font=("Arial", 11),
        bg="lightgray"
    ).pack(pady=10)
    
    tk.Entry(body, font=("Arial", 11), width=30).pack(pady=10)
    
    # Footer
    footer = tk.Frame(root, bg="darkgray")
    footer.pack(fill=tk.X, side=tk.BOTTOM)
    
    tk.Button(
        footer,
        text="Exit",
        command=root.quit,
        bg="red",
        fg="white",
        padx=20,
        pady=10
    ).pack(pady=10)
    
    root.mainloop()


# ============================================
# Example 5: Checkbutton and Radiobutton
# ============================================
def example_5_check_radio():
    """Working with checkbutton and radiobutton"""
    root = tk.Tk()
    root.title("Checkbutton and Radiobutton")
    root.geometry("400x300")
    
    # Title
    tk.Label(root, text="Select Your Preferences", font=("Arial", 14, "bold")).pack(pady=20)
    
    # Checkbuttons
    tk.Label(root, text="Languages:", font=("Arial", 11)).pack(anchor="w", padx=20)
    
    python_var = tk.BooleanVar()
    js_var = tk.BooleanVar()
    java_var = tk.BooleanVar()
    
    tk.Checkbutton(root, text="Python", variable=python_var).pack(anchor="w", padx=40)
    tk.Checkbutton(root, text="JavaScript", variable=js_var).pack(anchor="w", padx=40)
    tk.Checkbutton(root, text="Java", variable=java_var).pack(anchor="w", padx=40)
    
    # Radiobuttons
    tk.Label(root, text="Experience Level:", font=("Arial", 11)).pack(anchor="w", padx=20, pady=(20, 10))
    
    level_var = tk.StringVar(value="beginner")
    
    tk.Radiobutton(root, text="Beginner", variable=level_var, value="beginner").pack(anchor="w", padx=40)
    tk.Radiobutton(root, text="Intermediate", variable=level_var, value="intermediate").pack(anchor="w", padx=40)
    tk.Radiobutton(root, text="Advanced", variable=level_var, value="advanced").pack(anchor="w", padx=40)
    
    # Show selections
    def show_selections():
        msg = f"Python: {python_var.get()}\nJS: {js_var.get()}\nJava: {java_var.get()}\nLevel: {level_var.get()}"
        messagebox.showinfo("Your Selections", msg)
    
    tk.Button(root, text="Show Selections", command=show_selections, bg="blue", fg="white").pack(pady=20)
    
    root.mainloop()


# ============================================
# Example 6: Text Widget (Multi-line)
# ============================================
def example_6_text_widget():
    """Multi-line text widget"""
    root = tk.Tk()
    root.title("Text Widget")
    root.geometry("500x400")
    
    # Title
    tk.Label(root, text="Text Editor", font=("Arial", 14, "bold")).pack(pady=10)
    
    # Text widget
    text = tk.Text(
        root,
        font=("Arial", 11),
        height=12,
        width=50,
        wrap=tk.WORD
    )
    text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    
    # Insert some default text
    text.insert("1.0", "Type your message here...\n\n")
    
    # Button frame
    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=10)
    
    # Get text button
    def get_text():
        content = text.get("1.0", tk.END)
        messagebox.showinfo("Text Content", content)
    
    tk.Button(btn_frame, text="Get Text", command=get_text, bg="blue", fg="white").pack(side=tk.LEFT, padx=5)
    
    # Clear text button
    def clear_text():
        text.delete("1.0", tk.END)
    
    tk.Button(btn_frame, text="Clear", command=clear_text, bg="red", fg="white").pack(side=tk.LEFT, padx=5)
    
    root.mainloop()


# ============================================
# Example 7: Listbox
# ============================================
def example_7_listbox():
    """Working with listbox"""
    root = tk.Tk()
    root.title("Listbox Widget")
    root.geometry("400x350")
    
    # Title
    tk.Label(root, text="Programming Languages", font=("Arial", 14, "bold")).pack(pady=10)
    
    # Listbox with scrollbar
    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    
    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    listbox = tk.Listbox(
        frame,
        font=("Arial", 11),
        yscrollcommand=scrollbar.set
    )
    listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.config(command=listbox.yview)
    
    # Add items
    languages = ["Python", "JavaScript", "Java", "C++", "Go", "Rust", "PHP", "Ruby", "Swift", "Kotlin"]
    for lang in languages:
        listbox.insert(tk.END, lang)
    
    # Button frame
    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=10, fill=tk.X, padx=10)
    
    # Get selection
    def get_selection():
        selection = listbox.curselection()
        if selection:
            item = listbox.get(selection[0])
            messagebox.showinfo("Selected", f"You selected: {item}")
        else:
            messagebox.showwarning("Selection", "Please select an item!")
    
    tk.Button(btn_frame, text="Get Selection", command=get_selection, bg="green", fg="white").pack(side=tk.LEFT, padx=5)
    
    # Add item
    def add_item():
        new_lang = tk.simpledialog.askstring("Add Language", "Enter language name:")
        if new_lang:
            listbox.insert(tk.END, new_lang)
    
    tk.Button(btn_frame, text="Add", command=add_item, bg="blue", fg="white").pack(side=tk.LEFT, padx=5)
    
    root.mainloop()


# ============================================
# MAIN MENU
# ============================================
def main():
    """Main menu to run examples"""
    root = tk.Tk()
    root.title("Tkinter Examples Menu")
    root.geometry("500x400")
    
    # Title
    tk.Label(
        root,
        text="Tkinter Basics Examples",
        font=("Arial", 16, "bold"),
        bg="darkblue",
        fg="white",
        pady=20
    ).pack(fill=tk.X)
    
    # Examples
    examples = [
        ("1. Simple Window", example_1_simple_window),
        ("2. Label and Button", example_2_label_button),
        ("3. Text Entry", example_3_text_entry),
        ("4. Multiple Widgets", example_4_multiple_widgets),
        ("5. Check & Radio Buttons", example_5_check_radio),
        ("6. Text Widget", example_6_text_widget),
        ("7. Listbox", example_7_listbox),
    ]
    
    # Frame for buttons
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
            pady=10,
            width=30
        ).pack(pady=8)
    
    # Exit button
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

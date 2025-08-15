import tkinter as tk
from tkinter import messagebox
import db  # This is our database file with functions for add, get, update, delete

def launch_gui():
    # We will store the selected user ID here
    selected_user_id = [None]

    # ------------------- Helper Functions -------------------

    # Show all users in the Listbox
    def refresh_list():
        user_listbox.delete(0, tk.END)  # Clear the list first
        for user in db.get_users():  # Get all users from database
            user_listbox.insert(
                tk.END,
                f"{user[0]}: {user[1]} | {user[2]} | Subscribed: {user[3]}"
            )

    # When a user clicks on a name from the list
    def on_select(event):
        selection = user_listbox.curselection()
        if selection:
            index = selection[0]  # Which row was clicked
            user = db.get_users()[index]
            selected_user_id[0] = user[0]  # Store user ID
            # Fill the form with selected user details
            name_entry.delete(0, tk.END)
            name_entry.insert(0, user[1])
            gender_var.set(user[2])
            subscribe_var.set(user[3] == "Yes")

    # Add a new user to database
    def add_user():
        name = name_entry.get()
        gender = gender_var.get()
        subscribed = "Yes" if subscribe_var.get() else "No"

        if name == "":
            messagebox.showwarning("Input Error", "Name cannot be empty")
            return

        db.add_user(name, gender, subscribed)
        clear_fields()
        refresh_list()

    # Update existing user
    def update_user():
        if selected_user_id[0] is None:
            messagebox.showwarning("Select User", "No user selected")
            return
        name = name_entry.get()
        gender = gender_var.get()
        subscribed = "Yes" if subscribe_var.get() else "No"

        db.update_user(selected_user_id[0], name, gender, subscribed)
        clear_fields()
        refresh_list()

    # Delete selected user
    def delete_user():
        if selected_user_id[0] is None:
            messagebox.showwarning("Select User", "No user selected")
            return
        db.delete_user(selected_user_id[0])
        clear_fields()
        refresh_list()

    # Clear input fields
    def clear_fields():
        name_entry.delete(0, tk.END)
        gender_var.set("Male")
        subscribe_var.set(False)
        selected_user_id[0] = None
        user_listbox.selection_clear(0, tk.END)

    # ------------------- GUI Setup -------------------
    root = tk.Tk()
    root.title("CRUD App")
    root.geometry("500x600")
    root.configure(bg="#f0f4f7")

    label_font = ("Helvetica", 12, "bold")
    entry_font = ("Helvetica", 11)

    # ----- Form Frame -----
    form_frame = tk.Frame(root, bg="#f0f4f7")
    form_frame.pack(pady=10)

    # Name Input
    tk.Label(form_frame, text="Name:", font=label_font, bg="#f0f4f7").grid(row=0, column=0, sticky="w", padx=5, pady=5)
    name_entry = tk.Entry(form_frame, font=entry_font, width=30)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    # Gender Input
    gender_var = tk.StringVar(value="Male")
    tk.Label(form_frame, text="Gender:", font=label_font, bg="#f0f4f7").grid(row=1, column=0, sticky="w", padx=5)
    gender_frame = tk.Frame(form_frame, bg="#f0f4f7")
    gender_frame.grid(row=1, column=1, sticky="w")
    tk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male", bg="#f0f4f7").pack(side="left")
    tk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female", bg="#f0f4f7").pack(side="left")

    # Subscription Checkbox
    subscribe_var = tk.BooleanVar()
    tk.Checkbutton(form_frame, text="Subscribe to newsletter", variable=subscribe_var, bg="#f0f4f7").grid(row=2, columnspan=2, pady=5)

    # ----- Buttons -----
    button_frame = tk.Frame(root, bg="#f0f4f7")
    button_frame.pack(pady=10)

    tk.Button(button_frame, text="Add User", command=add_user, bg="#4CAF50", fg="white", width=15).grid(row=0, column=0, padx=5, pady=5)
    tk.Button(button_frame, text="Update User", command=update_user, bg="#2196F3", fg="white", width=15).grid(row=0, column=1, padx=5, pady=5)
    tk.Button(button_frame, text="Delete User", command=delete_user, bg="#f44336", fg="white", width=15).grid(row=1, column=0, padx=5, pady=5)
    tk.Button(button_frame, text="Clear Fields", command=clear_fields, bg="#9E9E9E", fg="white", width=15).grid(row=1, column=1, padx=5, pady=5)

    # ----- User List -----
    list_frame = tk.Frame(root, bg="#f0f4f7")
    list_frame.pack(pady=10)

    tk.Label(list_frame, text="User List (Click to Select):", font=label_font, bg="#f0f4f7").pack()
    user_listbox = tk.Listbox(list_frame, height=10, width=60, font=entry_font, bg="white", selectbackground="#cce5ff")
    user_listbox.pack()
    user_listbox.bind("<<ListboxSelect>>", on_select)

    # Load initial data
    refresh_list()

    # Close database on exit
    def on_close():
        db.close_db()
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()

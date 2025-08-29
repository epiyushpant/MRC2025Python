import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
from datetime import datetime

class BookInventoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Inventory Management")
        self.root.geometry("600x500")

        # Database setup
        self.conn = sqlite3.connect("books.db")
        self.cursor = self.conn.cursor()
        self.create_table()

        # GUI Elements
        self.create_widgets()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                genre TEXT,
                available BOOLEAN NOT NULL
            )
        ''')
        self.conn.commit()

    def create_widgets(self):
        # Labels and Entry Fields
        tk.Label(self.root, text="Book Title:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.title_entry = tk.Entry(self.root, width=30)
        self.title_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.root, text="Author:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.author_entry = tk.Entry(self.root, width=30)
        self.author_entry.grid(row=1, column=1, padx=5, pady=5)

        # Genre Radio Buttons
        tk.Label(self.root, text="Genre:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.genre_var = tk.StringVar(value="Fiction")
        genres = ["Fiction", "Non-Fiction", "Sci-Fi", "Mystery"]
        for i, genre in enumerate(genres):
            tk.Radiobutton(self.root, text=genre, variable=self.genre_var, value=genre).grid(row=2, column=i+1, padx=5)

        # Availability Checkbox
        self.available_var = tk.BooleanVar(value=True)
        tk.Checkbutton(self.root, text="Available", variable=self.available_var).grid(row=3, column=1, pady=5, sticky="w")

        # CRUD Buttons
        tk.Button(self.root, text="Add Book", command=self.add_book).grid(row=4, column=0, pady=10)
        tk.Button(self.root, text="Update Book", command=self.update_book).grid(row=4, column=1, pady=10)
        tk.Button(self.root, text="Delete Book", command=self.delete_book).grid(row=4, column=2, pady=10)
        tk.Button(self.root, text="Clear Fields", command=self.clear_fields).grid(row=4, column=3, pady=10)

        # Treeview for displaying books
        self.tree = ttk.Treeview(self.root, columns=("ID", "Title", "Author", "Genre", "Available"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Title", text="Title")
        self.tree.heading("Author", text="Author")
        self.tree.heading("Genre", text="Genre")
        self.tree.heading("Available", text="Available")
        self.tree.grid(row=5, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        # Scrollbar
        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.tree.yview)
        scrollbar.grid(row=5, column=4, sticky="ns")
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Load data
        self.load_data()

    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        genre = self.genre_var.get()
        available = self.available_var.get()

        if not title or not author:
            messagebox.showerror("Error", "Title and Author are required!")
            return

        self.cursor.execute("INSERT INTO books (title, author, genre, available) VALUES (?, ?, ?, ?)",
                          (title, author, genre, available))
        self.conn.commit()
        self.load_data()
        self.clear_fields()
        messagebox.showinfo("Success", "Book added successfully!")

    def update_book(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a book to update!")
            return

        book_id = self.tree.item(selected_item)["values"][0]
        title = self.title_entry.get()
        author = self.author_entry.get()
        genre = self.genre_var.get()
        available = self.available_var.get()

        if not title or not author:
            messagebox.showerror("Error", "Title and Author are required!")
            return

        self.cursor.execute("UPDATE books SET title = ?, author = ?, genre = ?, available = ? WHERE id = ?",
                          (title, author, genre, available, book_id))
        self.conn.commit()
        self.load_data()
        self.clear_fields()
        messagebox.showinfo("Success", "Book updated successfully!")

    def delete_book(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a book to delete!")
            return

        book_id = self.tree.item(selected_item)["values"][0]
        if messagebox.askyesno("Confirm", "Are you sure you want to delete this book?"):
            self.cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
            self.conn.commit()
            self.load_data()
            self.clear_fields()
            messagebox.showinfo("Success", "Book deleted successfully!")

    def load_data(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.cursor.execute("SELECT * FROM books")
        for row in self.cursor.fetchall():
            self.tree.insert("", "end", values=row)

    def on_tree_select(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            values = self.tree.item(selected_item)["values"]
            self.title_entry.delete(0, tk.END)
            self.title_entry.insert(0, values[1])
            self.author_entry.delete(0, tk.END)
            self.author_entry.insert(0, values[2])
            self.genre_var.set(values[3])
            self.available_var.set(values[4])

    def clear_fields(self):
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.genre_var.set("Fiction")
        self.available_var.set(True)

    def __del__(self):
        self.conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = BookInventoryApp(root)
    root.mainloop()
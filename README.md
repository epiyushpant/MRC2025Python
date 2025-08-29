# Book Inventory Management Application

## Overview
This is a Python application built using `tkinter` for a graphical user interface (GUI) and `sqlite3` for database management. The application allows users to manage a book inventory by performing CRUD (Create, Read, Update, Delete) operations on book records stored in a SQLite database.

## Features
- **Add Book**: Add a new book with title, author, genre, and availability status.
- **Update Book**: Modify the details of an existing book.
- **Delete Book**: Remove a book from the inventory with confirmation.
- **View Books**: Display all books in a table format with a scrollbar.
- **Clear Fields**: Reset input fields to default values.
- **Database Integration**: Uses SQLite to persistently store book data.
- **User-Friendly Interface**: Includes entry fields, radio buttons for genre selection, a checkbox for availability, and a treeview for displaying records.

## Requirements
- Python 3.x
- `tkinter` (usually included with Python standard library)
- `sqlite3` (included with Python standard library)

## Installation
1. Ensure Python 3.x is installed on your system.
2. No additional libraries are required as `tkinter` and `sqlite3` are part of the Python standard library.
3. Clone or download the script to your local machine.

## Usage
1. Save the script as `book_inventory.py`.
2. Run the script using Python:
   ```bash
   python3 book_inventory.py
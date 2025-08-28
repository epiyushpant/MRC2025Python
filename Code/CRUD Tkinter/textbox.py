# from tkinter import *

# root = Tk()

# entry = Entry(root)  # Create text box
# entry.pack()

# root.mainloop()


"""
| Option    | Purpose                                    | Example              |
| --------- | ------------------------------------------ | -------------------- |
| `width`   | Number of characters wide                  | `width=30`           |
| `fg`      | Text color                                 | `fg="blue"`          |
| `bg`      | Background color                           | `bg="lightyellow"`   |
| `font`    | Font style & size                          | `font=("Arial", 14)` |
| `show`    | Masks input (e.g., password)               | `show="*"`           |
| `state`   | `NORMAL` or `DISABLED`                     | `state=DISABLED`     |
| `justify` | Text alignment (`LEFT`, `CENTER`, `RIGHT`) | `justify=CENTER`     |


| Method                  | Purpose                          |
| ----------------------- | -------------------------------- |
| `.get()`                | Get the current text             |
| `.insert(index, text)`  | Insert text at position          |
| `.delete(start, end)`   | Delete text from start to end    |
| `.config(option=value)` | Change properties after creation |


"""


from tkinter import *

root = Tk()
root.title("Name Input")

def show_text():
    print("Entered:", entry.get())

entry = Entry(root, width=30, font=("Arial", 14))
entry.pack(pady=10)

Button(root, text="Show Text", command=show_text).pack()

root.mainloop()




"""
import tkinter as tk

def show_data():
    value1 = entry1.get()  # Get text from first textbox
    value2 = entry2.get()  # Get text from second textbox
    print("First box:", value1)
    print("Second box:", value2)

root = tk.Tk()
root.title("Two Entry Boxes")

# First Entry
tk.Label(root, text="First Name").pack()
entry1 = tk.Entry(root, width=30)
entry1.pack(pady=5)

# Second Entry
tk.Label(root, text="Last Name").pack()
entry2 = tk.Entry(root, width=30)
entry2.pack(pady=5)

# Button to fetch values
tk.Button(root, text="Show Data", command=show_data).pack(pady=10)

root.mainloop()


"""
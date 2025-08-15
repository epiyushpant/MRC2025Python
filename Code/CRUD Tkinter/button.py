
# def say_hello():
#     print("Hello!")


# import tkinter as tk
# root = tk.Tk()

# btn = tk.Button(root, text="Say Hello", command=say_hello)

# # btn.config(font=("Arial", 14), fg="white", bg="blue", padx=10, pady=5, relief="raised")
# # btn = tk.Button(root, text="Bigger", width=20, height=2)


# btn.pack()
# root.mainloop()


"""
| Option             | Purpose                          | Example                                                 |
| ------------------ | -------------------------------- | ------------------------------------------------------- |
| `text`             | Text displayed on button         | `text="Submit"`                                         |
| `command`          | Function executed when clicked   | `command=my_function`                                   |
| `fg`               | Text color                       | `fg="white"`                                            |
| `bg`               | Background color                 | `bg="blue"`                                             |
| `font`             | Font style & size                | `font=("Arial", 14, "bold")`                            |
| `width`, `height`  | Size in text units               | `width=15, height=2`                                    |
| `state`            | Normal, Disabled, or Active      | `state=DISABLED`                                        |
| `image`            | Display an image instead of text | `image=photo`                                           |
| `compound`         | Position text & image            | `compound="left"`                                       |
| `relief`           | Border style                     | `"flat"`, `"raised"`, `"sunken"`, `"groove"`, `"ridge"` |
| `borderwidth`      | Border thickness                 | `borderwidth=5`                                         |
| `activebackground` | Color when clicked               | `activebackground="green"`                              |
| `activeforeground` | Text color when clicked          | `activeforeground="yellow"`                             |


"""

""" 
from tkinter import *

root = Tk()

def greet():
    print("Welcome to Tkinter!")

btn = Button(
    root,
    text="Greet",
    command=greet,
    fg="white",
    bg="blue",
    font=("Helvetica", 14, "bold"),
    relief="raised",
    borderwidth=4,
    activebackground="green",
    activeforeground="yellow",
    width=15,
    height=2
)

# btn.config(state=DISABLED)

btn.pack(pady=10)



root.mainloop()


"""



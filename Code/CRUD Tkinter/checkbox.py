import tkinter as tk

root = tk.Tk()

subscribe_var = tk.BooleanVar()  # Variable to track checkbox state

check = tk.Checkbutton(root, text="Subscribe to newsletter", variable=subscribe_var)
check.pack()




"""
variable holds the state:
True if checked
False if unchecked
Use BooleanVar() for True/False.
Can also use IntVar() (1 if checked, 0 if unchecked).

"""


def show_state():
    if subscribe_var.get():
        print("Subscribed")
    else:
        print("Not Subscribed")

btn = tk.Button(root, text="Check Subscription", command=show_state)
btn.pack()

root.mainloop()

"""
| Option     | Purpose                       | Example                  |
| ---------- | ----------------------------- | ------------------------ |
| `text`     | Text label beside checkbox    | `text="Accept Terms"`    |
| `variable` | Holds checked state           | `variable=subscribe_var` |
| `onvalue`  | Value when checked            | `onvalue=1` (default)    |
| `offvalue` | Value when unchecked          | `offvalue=0` (default)   |
| `command`  | Function to call when toggled | `command=my_function`    |
| `fg`       | Text color                    | `fg="blue"`              |
| `bg`       | Background color              | `bg="lightgray"`         |
| `font`     | Font style                    | `font=("Arial", 12)`     |
| `state`    | Enabled/Disabled              | `state=tk.DISABLED`      |

"""



import tkinter as tk

root = tk.Tk()
root.title("Multiple Checkbuttons")

option1_var = tk.BooleanVar()
option2_var = tk.BooleanVar()

tk.Checkbutton(root, text="Option 1", variable=option1_var).pack()
tk.Checkbutton(root, text="Option 2", variable=option2_var).pack()

def show_choices():
    print("Option 1:", option1_var.get())
    print("Option 2:", option2_var.get())

tk.Button(root, text="Show Choices", command=show_choices).pack()

root.mainloop()

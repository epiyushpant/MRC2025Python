import tkinter as tk

root = tk.Tk()
root.title("Radiobutton Example")

# Variable to hold the selected option's value
gender_var = tk.StringVar(value="Male")  # default selected option

# Creating Radiobuttons
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").pack(anchor='w')
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").pack(anchor='w')
tk.Radiobutton(root, text="Other", variable=gender_var, value="Other").pack(anchor='w')

def show_selection():
    print("Selected Gender:", gender_var.get())

# Button to show the selected option
tk.Button(root, text="Show Selection", command=show_selection).pack(pady=10)

root.mainloop()


"""
variable is a shared variable (usually a StringVar or IntVar) among the group, which keeps track of the selected button.
value is the unique value assigned to each radiobutton.
When a radiobutton is selected, the variable gets updated with its value.
Only one radiobutton in the group can be selected at a time.
Use .get() on the variable to find out which option is selected.

| Option     | Purpose                                | Example                   |
| ---------- | -------------------------------------- | ------------------------- |
| `text`     | The text label displayed               | `text="Male"`             |
| `variable` | The shared variable for the group      | `variable=gender_var`     |
| `value`    | The value assigned when selected       | `value="Male"`            |
| `command`  | Function to call when selected         | `command=some_function`   |
| `fg`       | Text color                             | `fg="blue"`               |
| `bg`       | Background color                       | `bg="lightgray"`          |
| `font`     | Font style and size                    | `font=("Arial", 12)`      |
| `state`    | Enable or disable the button           | `state=tk.DISABLED`       |
| `anchor`   | Position of the text inside the button | `anchor='w'` (left align) |


"""
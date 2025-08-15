# from tkinter import *

# root = Tk()

# textbox = Text(root, height=5, width=40)
# textbox.pack()

# root.mainloop()



""" 
| Option   | Purpose                           | Example                |
| -------- | --------------------------------- | ---------------------- |
| `height` | Number of text lines              | `height=10`            |
| `width`  | Number of characters per line     | `width=50`             |
| `wrap`   | Wrap mode: `WORD`, `CHAR`, `NONE` | `wrap=WORD`            |
| `fg`     | Text color                        | `fg="green"`           |
| `bg`     | Background color                  | `bg="lightgrey"`       |
| `font`   | Font style                        | `font=("Courier", 12)` |
| `state`  | Editable or not                   | `state=DISABLED`       |


| Method                 | Purpose                       |
| ---------------------- | ----------------------------- |
| `.get(start, end)`     | Get text (e.g., `"1.0", END`) |
| `.insert(index, text)` | Insert at given position      |
| `.delete(start, end)`  | Delete text from range        |
| `.config()`            | Change properties dynamically |


"""

from tkinter import *

root = Tk()
root.title("Multi-line Input")

def show_content():
    print(textbox.get("1.0", END))  # From line 1, char 0 to end

textbox = Text(root, height=5, width=40, font=("Arial", 12))
textbox.pack(pady=10)

Button(root, text="Show Content", command=show_content).pack()

root.mainloop()      


"""
Entry = Single-line input
Text = Multi-line input
.get() is different for Entry (no indexes) vs Text (needs start & end positions)
show="*" in Entry is useful for passwords
state=DISABLED makes text read-only
"""

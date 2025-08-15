# import tkinter as tk

# root = tk.Tk()
# root.title("Label Example")
# label = tk.Label(root, text="Hello, I am a Label!", font=("Arial", 14), fg="blue")
# label.pack(pady=10)

# root.mainloop()

"""

| Option            | Purpose                                                                | Example                      |
| ----------------- | ---------------------------------------------------------------------- | ---------------------------- |
| `text`            | The text to display                                                    | `text="Welcome"`             |
| `font`            | Font family, size, style                                               | `font=("Arial", 14, "bold")` |
| `fg`              | Text color                                                             | `fg="blue"`                  |
| `bg`              | Background color                                                       | `bg="yellow"`                |
| `width`, `height` | Size in text units                                                     | `width=20, height=2`         |
| `padx`, `pady`    | Padding inside label                                                   | `.pack(padx=10, pady=5)`     |
| `anchor`          | Align text (`"w"`, `"e"`, `"center"`)                                  | `anchor="w"`                 |
| `relief`          | Border style (`"flat"`, `"raised"`, `"sunken"`, `"groove"`, `"ridge"`) | `relief="groove"`            |

"""


import tkinter as tk

root = tk.Tk()
root.title("Label Styling")

label = tk.Label(
    root,
    text="This is a styled label",
    font=("Helvetica", 16, "italic"),
    fg="white",
    bg="black",
    width=30,
    height=2,
    relief="relief"
)
label.pack(pady=10) 


root.mainloop()


"""


pack() — Placing Widgets in the Window

In Tkinter, widgets (Labels, Buttons, etc.) don’t show up just by creating them —
you must add them to the window using a geometry manager.
There are three geometry managers:
pack() → Places widgets in blocks (top, bottom, left, right)
grid() → Places widgets in a table-like grid
place() → Places widgets at exact x, y coordinates

mainloop() — Running the Application
Tkinter works in an event loop:
It waits for events (button clicks, mouse movement, key presses).
It updates the GUI whenever needed.
It keeps the window open until you close it.


"""


# Exampleof using pack geometry manager in Tkinter
# import tkinter as tk

# root = tk.Tk()
# root.title("Pack Example")

# tk.Label(root, text="Top", bg="red").pack(side="top", fill="x")
# tk.Label(root, text="Left", bg="green").pack(side="left", fill="y")
# tk.Label(root, text="Right", bg="blue").pack(side="right", fill="y")
# tk.Label(root, text="Bottom", bg="yellow").pack(side="bottom", fill="x")

# root.mainloop()


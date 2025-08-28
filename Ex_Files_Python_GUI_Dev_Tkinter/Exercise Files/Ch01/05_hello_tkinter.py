#!/usr/bin/python3
# hello_tkinter.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *

root = Tk()
Label(root, text="Hello, Tkinter!").pack() #pack means "put this widget in the window"
root.mainloop() # The mainloop() method is what keeps the window open
# until the user closes it.

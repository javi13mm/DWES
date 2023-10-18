from tkinter import ttk
import tkinter as tk

def showDetail(cell):
    root = tk.Toplevel()
    root.title("Información")

    label = ttk.Label(root, image = cell.img)
    label.pack()
    label1 = ttk.Label(root, text = cell.name)
    label1.pack()
    label2 = ttk.Label(root, text = cell.desc)
    label2.pack()

    root.mainloop()
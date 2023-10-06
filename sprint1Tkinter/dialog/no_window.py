from tkinter import Tk, ttk

def showNo():
    root = Tk()
    root.title("NoWindow")
    label = ttk.Label(root, text = "No, qué asco!")
    label.pack()
    root.mainloop()
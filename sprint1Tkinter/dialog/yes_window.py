from tkinter import Tk, ttk

def showYes():
    root = Tk()
    root.title("YesWindow")
    label = ttk.Label(root, text = "Sí, qué ricos!")
    label.pack()
    root.mainloop()
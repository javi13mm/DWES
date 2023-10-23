from tkinter import ttk
import tkinter as tk

def showDetail(cell):
    root = tk.Toplevel()
    root.title("Información")
    root.resizable(False, False)

    ancho = 330
    alto = 230
    root.geometry(f"{int(ancho)}x{int(alto)}")

    # si implementamos este código, ancho y alto de la ventana serán números accesibles por winfo:
    root.config(width=ancho, height=alto)
    x = (root.winfo_screenwidth() - root.winfo_reqwidth())/2
    y = (root.winfo_screenheight() - root.winfo_reqheight())/2
    root.geometry(f"+{int(x)}+{int(y)}")

    label = ttk.Label(root, image = cell.img)
    label.pack(pady=[10,0])
    label1 = ttk.Label(root, text = cell.name)
    label1.pack()
    label2 = ttk.Label(root, text = cell.desc, wraplength=320)
    label2.pack(pady=10, padx=5, anchor="w")

    root.mainloop()
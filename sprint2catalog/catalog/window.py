from tkinter import ttk, messagebox
import tkinter as tk
from cell import Cell
from detail_window import showDetail

class MainWindow():
    cells = []        

    def __init__(self, root, json_data):
        for tenista in json_data:
            name = tenista.get("name")
            description = tenista.get("description")
            image_url = tenista.get("image_url")

            cell = Cell(name,description,image_url)

            self.cells.append(cell)

        root.title("MainWindow")
        root.resizable(False, False)

        # ancho y alto iguales:
        dimension = 250
        root.geometry(f"{int(dimension)}x{int(dimension)}")

        # si implementamos este código, ancho y alto de la ventana serán números accesibles por winfo:
        root.config(width=dimension, height=dimension)
        x = (root.winfo_screenwidth() - root.winfo_reqwidth())/2
        y = (root.winfo_screenheight() - root.winfo_reqheight())/2
        root.geometry(f"+{int(x)}+{int(y)}")

        # implementación de menú:
        barra_menus = tk.Menu()
        # sección ayuda del menú
        ayuda = tk.Menu(barra_menus, tearoff=False)
        # función de 'Acerca de'
        ayuda.add_command(
            label="Acerca de",
            accelerator="Ctrl+A",
            command=archivo_nuevo_presionado
        )
        # atajo teclado para función 'Acerca de':
        root.bind_all("<Control-a>", archivo_nuevo_presionado)
        barra_menus.add_cascade(menu=ayuda, label="Ayuda")
        root.config(menu=barra_menus)

        # implementación scrollbar:
        self.canvas = tk.Canvas(root, highlightthickness=0)
        self.scrollbar = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview, width=15)
        self.scrollable_frame = tk.Frame(self.canvas, background="gray10")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0,0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        for i, cell in enumerate(self.cells):
            frame = tk.Frame(self.scrollable_frame, background="gray10")
            frame.pack(pady=10)

            label = ttk.Label(frame, image = cell.img, text = cell.name, compound = tk.BOTTOM, background="gray10" , foreground="white")
            label.grid(row = 0, column = 0, padx=(root.winfo_reqwidth()-self.scrollbar.winfo_reqwidth()-cell.img.width())/2)
            label.bind(
                "<Button-1>",
                lambda event,
                cell = cell: showDetail(cell)
            )
        
        self.canvas.grid(row = 0, column = 0, sticky="nsew")
        self.scrollbar.grid(row = 0, column = 1, sticky="ns")

        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)

# función despliegue messagebox del menú
# 'event=None' es cenesario para que el atajo de teclado funcione
def archivo_nuevo_presionado(event=None):
    message = "Este programa está desarrollado por J.M., un simple aficionado del tenis."
    messagebox.showinfo("Información", message)

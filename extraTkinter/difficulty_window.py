import tkinter as tk

class DifficultyWindow:
    # Dimensiones pantalla carga:
    width = 320
    height = 165

    # Variable elección:
    choice = ""

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Ahorcado")

        # Establecimiento dimensiones:
        self.root.geometry(f"{int(self.width)}x{int(self.height)}")
        self.root.resizable(False, False)
        self.root.config(width=self.width, height=self.height, bg="navy")
        self.root.geometry(f"+{int((self.root.winfo_screenwidth()-self.width)/2)}+{int((self.root.winfo_screenheight()-self.height)/2)}")

        label = tk.Label(self.root, text="SELECCIONE NIVEL DE DIFICULTAD:", fg="lightgray", font="System", background="navy")
        label.pack()

        # Botones opciones:
        button1 = tk.Button(
            self.root,
            width=6,
            text="FÁCIL",
            fg="gray15",
            background="lightgray",
            font="System",
            activeforeground="gray5",
            activebackground="gray",
            name="facil",
            command=lambda:self.funcion(button1.cget("text"))
        )
        button2 = tk.Button(
            self.root,
            width=6,
            text="MEDIO",
            fg="gray15",
            background="lightgray",
            font="System",
            activeforeground="gray5",
            activebackground="gray",
            name="medio",
            command=lambda:self.funcion(button2.cget("text"))
        )
        button3 = tk.Button(
            self.root,
            width=6,
            text="DIFÍCIL",
            fg="gray15",
            background="lightgray",
            font="System",
            activeforeground="gray5",
            activebackground="gray",
            name="dificil",
            command=lambda:self.funcion(button3.cget("text"))
        )
        button4 = tk.Button(
            self.root,
            text="SALIR",
            fg="lightgray",
            background="red",
            font="System",
            activeforeground="gray",
            activebackground="red4",
            name="salir",
            command=lambda:self.funcion(button4.cget("text"))
        )

        button1.pack(anchor="n", pady=5)
        button2.pack(anchor="n")
        button3.pack(anchor="n", pady=5)
        button4.pack(side="bottom", anchor="e", pady=(15,5), padx=(5))
        
        self.root.mainloop()

    # Función click botón:
    def funcion(self, button_name):
        if button_name == "DIFÍCIL":
            self.choice = "dificil"
        elif button_name == "MEDIO":
            self.choice = "medio"
        elif button_name == "FÁCIL":
            self.choice = "facil"
        else:
            self.choice = "salir"
        self.root.destroy()
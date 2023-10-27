import tkinter as tk
from random import randint
from PIL import ImageTk

class GameWindow:
    # Dimensiones pantalla carga:
    width = 750
    height = 400

    def __init__(self, choice, images, palabras_json):
        self.root = tk.Tk()
        self.root.title("Ahorcado")

        # Establecimiento dimensiones:
        self.root.geometry(f"{int(self.width)}x{int(self.height)}")
        self.root.resizable(False, False)
        self.root.config(width=self.width, height=self.height)
        self.root.geometry(f"+{int((self.root.winfo_screenwidth()-self.width)/2)}+{int((self.root.winfo_screenheight()-self.height)/2)}")

        # Boolean victoria/derrota:
        self.victory = False
        self.game_over = False

        # Letra intento:
        self.letra = ""
        self.primera_letra = True

        # Variables partida:
        self.acierto = False
        self.aciertos = 0
        self.fallos = 0
        self.intentos = ""

        # Selección aleatoria de palabra a adivinar:
        index = randint(0,len(palabras_json[choice])-1)
        self.palabra = palabras_json[choice][index]

        # Inizialización de huecos:
        self.huecos = []
        for i in range(len(self.palabra)):
            self.huecos.append('_ ')

        # Guardado de imágenes como ImageTk:
        self.images = []
        for i in range(7):
            img = ImageTk.PhotoImage(images[i].img)
            self.images.append(img)

        # Dibujado de elementos:
        self.draw_window()

        self.root.mainloop()
    
    # Computación de letra introducida:
    def intro_letra(self):
        if not self.victory and not self.game_over:
            self.acierto = False

            # Obtención de letra de entrada y borrado de widget Entry:
            self.letra = self.entry.get().upper()
            self.entry.delete(0,tk.END)

            # Comprobación acierto o fallo:
            if not self.letra.isalpha() or len(self.letra) != 1 or self.intentos.find(self.letra) >= 0:
                pass
            else:
                for i in range(len(self.palabra)):
                    if (self.letra == self.palabra[i]):
                        # En caso de acertar una letra:
                        self.huecos[i] = self.letra+' '
                        self.aciertos += 1
                        # Añadimos letra a intentos en caso de acierto:
                        if not self.acierto:
                            self.acierto = True
                            if self.primera_letra:
                                self.intentos += self.letra
                                self.primera_letra = False
                            else:
                                self.intentos += ", "+self.letra
                    elif (i == len(self.palabra)-1) & (not self.acierto):
                        # En caso de recorrer la palabra y no acertar una letra:
                        self.fallos += 1
                        # Añadimos letra a intentos en caso de fallo:
                        if self.primera_letra:
                            self.intentos += self.letra
                            self.primera_letra = False
                        else:
                            self.intentos += ", "+self.letra
                
                # Comprobación partida finalizada:
                if self.fallos == 6:
                    self.huecos = []
                    for i in range(len(self.palabra)):
                        self.huecos.append(self.palabra[i]+' ')
                    # Cerrar ventana con boolean victoria a false:
                    self.game_over = True
                elif self.aciertos == len(self.palabra):
                    # Cerrar ventana con boolean victoria a true:
                    self.victory = True

                # Borrado y redibujado de elementos:
                self.canvas1.destroy()
                self.canvas2.destroy()
                self.canvas3.destroy()
                self.canvas4.destroy()
                self.draw_window()

    # Convertir Array de huecos a String:
    def escribir(self, huecos):
        lineas = ""
        for i in range(0, len(huecos)):
            lineas += huecos[i]
        return lineas

    def draw_window(self):
        # Dibujado de elementos:
        # Primer lienzo:
        self.canvas1 = tk.Canvas(self.root, bg="navy", highlightthickness=0, width=self.width, height=self.height)
        self.canvas1.pack(fill="both")
        # Segundo lienzo:
        self.canvas2 = tk.Canvas(self.root, bg="navy", highlightthickness=0, width=self.width, height=self.height)
        self.canvas2.pack(fill="both")
        #Tercer lienzo:
        self.canvas3 = tk.Canvas(self.root, bg="navy", highlightthickness=0, width=self.width, height=self.height)
        self.canvas3.pack(fill="both")
        # Cuarto lienzo:
        self.canvas4 = tk.Canvas(self.root, bg="navy", highlightthickness=0, width=self.width, height=self.height)
        self.canvas4.pack(fill="both", expand=tk.YES)

        # Label imágen:
        label1 = tk.Label(self.canvas1, image=self.images[self.fallos], highlightthickness=0, border=0)
        label1.pack(pady=30)
        
        # Label huecos:
        label2 = tk.Label(self.canvas2, text=self.escribir(self.huecos), font=("System",24), foreground="lightgray", bg=self.canvas2.cget("bg"))
        label2.pack(side="left", padx=(20,0))
        # Label errores:
        if self.victory:
            color = "lime"
        elif self.game_over:
            color = "red1"
        else:
            color = "lightgray"
        label3 = tk.Label(self.canvas2, text=(f"Errores: {int(self.fallos)}"), font=("System",24), foreground=color, bg=self.canvas2.cget("bg"))
        label3.pack(side="right", padx=(0,20))

        # Label letras falladas:
        label4 = tk.Label(self.canvas3, text="Letras intentadas: "+self.intentos, font=("System",12), foreground="lightgray", bg=self.canvas3.cget("bg"))
        label4.pack(pady=(15,0), padx=20, side="left")

        if not self.victory and not self.game_over:
            # Widget entry:
            self.entry = tk.Entry(self.canvas4, font=("System",12), justify="center", width=6)
            # Widget botón:
            button = tk.Button(
                self.canvas4,
                text="ENTER",
                font=("System",12),
                fg="gray15",
                background="lightgray",
                activeforeground="gray5",
                activebackground="gray",
                name="enter",
                command=self.intro_letra
            )
            button.pack(side="right", padx=(0,20))
            self.entry.pack(side="right", padx=(0,3))

        if self.victory or self.game_over:
            if self.victory:
                texto = "VICTORIA!"
                color = "lime"
            else:
                texto = "Derrota..."
                color = "red1"
            label_end = tk.Label(self.canvas4, text=texto, font=("System", 24), foreground=color, bg=self.canvas4.cget("bg"))
            button_end = tk.Button(
                self.canvas4,
                text="BACK",
                font=("System",12),
                fg="gray15",
                background="lightgray",
                activeforeground="gray5",
                activebackground="gray",
                name="back",
                command=self.root.destroy
            )
            button_end.pack(side="right", padx=(0,20))
            label_end.pack(side="right", padx=(0,3))
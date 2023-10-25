import tkinter as tk
import threading
import requests

class LoadingWindow:
    # Url palabras.json:
    json_url = "https://raw.githubusercontent.com/javi13mm/DWES/main/recursos/palabras.json"
    json_data = {}

    # Dimensiones pantalla carga:
    width = 320
    height = 240

    # Variables para efecto de carga:
    ini = -12
    fin = 0

    # Booleano control descarga datos:
    finish = False

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Ahorcado")

        # Establecimiento dimensiones:
        self.root.geometry(f"{int(self.width)}x{int(self.height)}")
        self.root.resizable(False, False)
        self.root.config(width=self.width, height=self.height, bg="gray3")
        self.root.geometry(f"+{int((self.root.winfo_screenwidth()-self.width)/2)}+{int((self.root.winfo_screenheight()-self.height)/2)}")

        # Canvas con texto y barra de carga:
        self.canvas = tk.Canvas(self.root, background="gray3", highlightthickness=0, width=self.width, height=self.height)
        self.canvas.pack()
        self.canvas.create_text((self.width/2, 98), text="CARGANDO PALABRAS", font=("System", 12), fill="gray90", anchor="center", tags="texto")
        # Rectángulo que rodea la barra de carga:
        self.canvas.create_rectangle((40, self.height/2-8), (self.width-36, self.height/2+8), width=2, outline="gray90")

        # Dibujo barra de carga:
        self.update_bar()

        # Comprobación descarga json:
        self.check_thread()

        # Hilo secundario descarga:
        self.thread = threading.Thread(target=self.fetch_json_data).start()

        self.root.mainloop()
        
    def draw_bar(self):
        # Barra de carga de cuadrados de 8x8px (240px de largo):
        self.canvas.create_line((44+self.ini, self.height/2), (44+self.fin, self.height/2), fill="gray90", width=8, tags="linea")

    def update_bar(self):
        # Actualizar inicio y fin para cada cuadrado de la barra:
        if self.ini < 228:
            self.ini += 12
            self.fin = self.ini + 8

        self.draw_bar()
        self.root.after(200, self.update_bar)
    
    def check_thread(self):
        # Si la descarga terminó, la ventana de carga se cierra:
        if self.finish:
            self.root.destroy()
        else:
            # La comprobación espera a que acabe la barra de carga:
            self.root.after(4100, self.check_thread)
    
    def fetch_json_data(self):
        response = requests.get(self.json_url)
        if response.status_code == 200:
            self.json_data = response.json()
            self.finish = True
import tkinter as tk
import threading
import requests
from image_class import ImageClass

class LoadingWindow:
    # Jsons para palabras:
    palabras_json = {}
    # Array de Objetos Image
    images = []
    # Booleanos control descarga datos:
    palabras_finish = False
    images_finish = False

    # Dimensiones pantalla carga:
    width = 320
    height = 240

    # Variables para efecto de carga:
    ini = -12
    fin = 0

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Ahorcado")

        # Establecimiento dimensiones:
        self.root.geometry(f"{int(self.width)}x{int(self.height)}")
        self.root.resizable(False, False)
        self.root.config(width=self.width, height=self.height)
        self.root.geometry(f"+{int((self.root.winfo_screenwidth()-self.width)/2)}+{int((self.root.winfo_screenheight()-self.height)/2)}")

        # Canvas con texto y barra de carga:
        self.canvas = tk.Canvas(self.root, background="navy", highlightthickness=0, width=self.width, height=self.height)
        self.canvas.pack()
        self.canvas.create_text((self.width/2, 98), text="CARGANDO IMÁGENES Y PALABRAS...", font=("System", 12), fill="lightgray", anchor="center", tags="texto")
        # Rectángulo que rodea la barra de carga:
        self.canvas.create_rectangle((38, self.height/2-8), (self.width-38, self.height/2+8), width=2, outline="lightgray")
        # Dibujo barra de carga:
        self.update_bar()

        # Comprobación descarga json:
        self.check_thread()

        # Hilo secundario descarga:
        self.thread = threading.Thread(target=self.fetch_json_data).start()

        self.root.mainloop()
        
    def draw_bar(self):
        # Barra de carga de cuadrados de 8x8px (240px de largo):
        self.canvas.create_line((42+self.ini, self.height/2), (42+self.fin, self.height/2), fill="lightgray", width=8, tags="linea")

    def update_bar(self):
        # Actualizar inicio y fin para cada cuadrado de la barra:
        if self.ini < 228:
            self.ini += 12
            self.fin = self.ini + 8

        self.draw_bar()
        self.root.after(500, self.update_bar)
    
    def check_thread(self):
        # Si las descargas terminaron, la ventana de carga se cierra:
        if self.palabras_finish & self.images_finish:
            self.root.destroy()
        else:
            # La comprobación espera a que acabe la barra de carga:
            self.root.after(5000, self.check_thread)
    
    def fetch_json_data(self):
        # Descarga palabras.json:
        response_palabras = requests.get("https://raw.githubusercontent.com/javi13mm/DWES/main/recursos/palabras.json")
        if response_palabras.status_code == 200:
            self.palabras_json = response_palabras.json()
            self.palabras_finish = True
        # Descargar y guardar imágenes en lista de Objetos Image:
        response_images = requests.get("https://raw.githubusercontent.com/javi13mm/DWES/main/recursos/ahorcado_images.json")
        if response_palabras.status_code == 200:
            for i in range(7):
                self.images.append(ImageClass(response_images.json().get(f"{int(i)}")))
            self.images_finish = True
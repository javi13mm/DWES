import tkinter as tk
import threading
import requests
import math
from window import MainWindow

class LoadingWindow:
    json_data = []

    def __init__(self, root):
        self.root = root
        self.root.title("Cargando...")
        self.root.resizable(False, False)

        ancho = 330
        alto = 140
        self.root.geometry(f"{int(ancho)}x{int(alto)}")

        # si implementamos este código, ancho y alto de la ventana serán números accesibles por winfo:
        self.root.config(width=ancho, height=alto)
        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth())/2
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight())/2
        self.root.geometry(f"+{int(x)}+{int(y)}")

        self.label = tk.Label(self.root, text="Cargando datos...", font=("Courier",14))
        self.label.pack(side=tk.TOP, pady=10)
        
        self.canvas = tk.Canvas(self.root, width=80, height=80)
        self.canvas.pack()

        # necesitamos 3 variables para generar un efecto de aceleración en la barra de carga:
        self.progress = 0
        self.inicio = 0
        self.start = 0
        self.vuelta = False

        self.draw_progress_circle()

        self.update_progress_circle()

        self.finish = False

        self.check_thread()

        self.thread = threading.Thread(target=self.fetch_json_data)
        self.thread.start()
    
    def draw_progress_circle(self):
        self.canvas.delete("arco")
        start = self.start
        progress = self.progress*360
        # para que la barra no desaparezca al llegar al final, variamos su posición, causando efecto de giro completo:
        if progress == 360:
            self.vuelta = True
            progress = 359.9
        elif progress == -360:
            self.vuelta = False
            progress = -359.9
        elif progress == 0:
            self.vuelta = False

        self.canvas.create_arc(10, 10, 70, 70,
                               start=start, extent=progress, tags="arco", outline='royalblue', width=4, style=tk.ARC)
    
    def update_progress_circle(self):
        # si todavía no se ha completado una vuelta, el sentido de la barra será antihorario:
        if not self.vuelta:
            self.progress = abs(math.sin(math.radians(self.inicio/2)))
        # si se ha completado una vuelta, el sentido de la barra será horario:
        else:
            self.progress = -abs(math.sin(math.radians(self.inicio/2)))

        # velocidad de la barra:
        self.inicio += 2
        if self.inicio >= 360:
            self.inicio -= 360

        # punto de inicio móvil de la barra:
        self.start += 10
        if self.start >= 360:
            self.start -= 360

        self.draw_progress_circle()
        self.root.after(10, self.update_progress_circle)
    
    def fetch_json_data(self):
        response = requests.get("https://raw.githubusercontent.com/javi13mm/DWES/main/recursos/catalog.json")
        if response.status_code == 200:
            self.json_data = response.json()
            self.finish = True
        
    def check_thread(self):
        if self.finish:
            self.root.destroy()
            launch_main_window(self.json_data)
        else:
            self.root.after(100, self.check_thread)

def launch_main_window(json_data):
    root = tk.Tk()
    app = MainWindow(root, json_data)
    root.mainloop()
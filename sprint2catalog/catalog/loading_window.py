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
        self.root.geometry("360x180")
        self.root.resizable(False, False)

        self.label = tk.Label(self.root, text="Cargando datos...", font=("Courier",14))
        self.label.pack(side=tk.TOP, pady=10)

        label_bg_color = self.label.cget("bg")
        
        self.canvas = tk.Canvas(self.root, width=120, height=120, bg=label_bg_color)
        self.canvas.pack()

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
        if progress == 360:
            self.vuelta = True
            progress = 359.9
        elif progress == -360:
            self.vuelta = False
            progress = -359.9
        elif progress == 0:
            self.vuelta = False

        self.canvas.create_arc(10, 10, 110, 110,
                               start=start, extent=progress, tags="arco", outline='royalblue', width=5, style=tk.ARC)
    
    def update_progress_circle(self):
        if not self.vuelta:
            self.progress = abs(math.sin(math.radians(self.inicio/2)))
        else:
            self.progress = -abs(math.sin(math.radians(self.inicio/2)))

        self.inicio += 2
        if self.inicio >= 360:
            self.inicio -= 360

        self.start += 10
        if self.start >= 360:
            self.start -= 360

        self.draw_progress_circle()
        self.root.after(15, self.update_progress_circle)
    
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
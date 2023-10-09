from tkinter import ttk
import tkinter as tk
from cell import Cell
from detail_window import showDetail

class MainWindow():

    def on_button_clicked(self, cell):
        showDetail(cell)

    def __init__(self, root): # self en python es como this en java
        root.title("MainWindow")
        self.cells = [
            Cell("Roger Federer", "C:\\msys64\\home\\Alumno\\DWES\\sprint1Tkinter\\catalog\\data\\unedited\\federer.jpg",
                        "Roger Federer es un extenista suizo, considerado uno de los mejores de todos los tiempos. Ha sido ganador de 20 torneos"+
                        " de Grand Slam. Destaca por dominar todas las facetas del juego."),
            Cell("Rafa Nadal", "C:\\msys64\\home\\Alumno\\DWES\\sprint1Tkinter\\catalog\\data\\unedited\\nadal.jpg",
                        "Rafael Nadal (\"El Matador\") es un tenista español, considerado uno de los mejores de todos los tiempos. Ha sido ganador de 22 torneos"+
                        " de Grand Slam. Destaca por su estilo de juego defensivo."),
            Cell("Novak Djokovic", "C:\\msys64\\home\\Alumno\\DWES\\sprint1Tkinter\\catalog\\data\\unedited\\djokovic.jpg",
                        "Novak Djokovic (\"Djoker\") es un tenista serbio, considerado uno de los mejores de todos los tiempos. Ha sido ganador de 24 torneos"+
                        " de Grand Slam. Destaca por sus golpes desde el fondo de la pista."),
            Cell("Andy Murray", "C:\\msys64\\home\\Alumno\\DWES\\sprint1Tkinter\\catalog\\data\\unedited\\murray.jpg",
                        "Andy Murray (\"Muzza\") es un tenista escocés, considerado uno de los mejores de las últimas décadas. Ha sido ganador de 3 torneos"+
                        " de Grand Slam. Destaca por su estilo de juego defensivo."),
            Cell("Serena Williams", "C:\\msys64\\home\\Alumno\\DWES\\sprint1Tkinter\\catalog\\data\\unedited\\serena.jpg",
                        "Serena Williams (\"Meka\") es una tenista estadounidense, considerada la mejor de toda la historia. Ha sido ganadora de 23 torneos"+
                        " de Grand Slam. Destaca por su gran potencia de golpeo.")
        ]

        for i, cell in enumerate(self.cells):
            label = ttk.Label(root, image = cell.image_tk, text = cell.title, compound = tk.BOTTOM)
            label.grid(row = i, column = 0)
            label.bind("<Button-1>", lambda event, cell = cell: self.on_button_clicked(cell))
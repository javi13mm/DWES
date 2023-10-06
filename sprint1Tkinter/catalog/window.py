from tkinter import ttk
import tkinter as tk
from cell import Cell
from PIL import Image
from tkinter import messagebox

class MainWindow():

    def on_button_clicked(self,cell):
        message = "Has hecho click en la celda "+cell.title
        messagebox.showinfo("Información", message)

    def __init__(self, root): # self en python es como this en java
        root.title("MainWindow")

        self.cells = [
            Cell("Roger Federer", "C:\\msys64\\home\\Alumno\\DWES\\sprint1Tkinter\\catalog\\data\\edited\\federer.jpg"),
            Cell("Rafa Nadal", "C:\\msys64\\home\\Alumno\\DWES\\sprint1Tkinter\\catalog\\data\\edited\\nadal.jpg"),
            Cell("Novak Djokovic", "C:\\msys64\\home\\Alumno\\DWES\\sprint1Tkinter\\catalog\\data\\edited\\djokovic.jpg"),
            Cell("Andy Murray", "C:\\msys64\\home\\Alumno\\DWES\\sprint1Tkinter\\catalog\\data\\edited\\murray.jpg"),
            Cell("Serena Williams", "C:\\msys64\\home\\Alumno\\DWES\\sprint1Tkinter\\catalog\\data\\edited\\serena.jpg")
        ]

        for i, cell in enumerate(self.cells):
            label = ttk.Label(root, image = cell.image_tk, text = cell.title, compound = tk.BOTTOM)
            label.grid(row = i, column = 0)
            label.bind("<Button-1>", lambda event, cell = cell: self.on_button_clicked(cell))
from tkinter import ttk
import tkinter as tk
from cell import Cell
from detail_window import showDetail

class MainWindow():
    def on_button_clicked(self, cell):
        showDetail(cell)

    def __init__(self, root, json_data): # self en python es como this en java
        root.title("MainWindow")

        self.cells = []

        for tenista in json_data:
            name = tenista.get("name")
            description = tenista.get("description")
            image_url = tenista.get("image_url")

            cell = Cell(name,description,image_url)

            self.cells.append(cell)

        for i, cell in enumerate(self.cells):
            label = ttk.Label(root, image = cell.img, text = cell.name, compound = tk.BOTTOM)
            label.grid(row = i, column = 0)
            label.bind("<Button-1>", lambda event, cell = cell: self.on_button_clicked(cell))
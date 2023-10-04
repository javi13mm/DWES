from tkinter import Tk, ttk
import tkinter as tk
from yes_window import showYes
from no_window import showNo

class MainWindow():

    def __init__(self, root):
        root.title("MainWindow")
        self.root = root

        self.frame = ttk.Frame(self.root)
        self.frame.pack(anchor = "nw")

        self.label = ttk.Label(self.frame, text = "Te gustan los pepinillos?")
        self.label.pack(anchor = "nw", padx = 4)
        
        self.button1 = ttk.Button(self.frame, text = "Yes", command = showYes)
        self.button1.pack(side = "left")

        self.button2 = ttk.Button(self.frame, text = "No", command = showNo)
        self.button2.pack(side = "right", padx = 5)


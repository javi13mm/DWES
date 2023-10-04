from tkinter import Tk, ttk

class MainWindow():
    def on_button_click(self):
        pass

    def __init__(self, root):
        root.title("MainWindow")
        self.root = root

        self.frame = ttk.Frame(self.root)
        self.frame.pack()

        self.label = ttk.Label(self.frame, text = "Message in label")
        self.label.pack()
        
        self.button = ttk.Button(self.frame, text = "Button", command = self.on_button_click)
        self.button.pack()


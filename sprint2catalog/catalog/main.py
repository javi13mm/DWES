from tkinter import Tk
from loading_window import LoadingWindow
from window import MainWindow

if __name__ == "__main__":
    root = Tk()
    app = LoadingWindow(root)
    root.mainloop()
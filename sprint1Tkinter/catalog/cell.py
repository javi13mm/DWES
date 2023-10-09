from PIL import ImageTk, Image

class Cell:
    def __init__(self, title, path, desc):
        self.title = title
        self.path = path
        self.desc = desc
        img = Image.open(self.path)
        imagen_redimensionada = img.resize((100,100),Image.Resampling.LANCZOS)
        self.image_tk = ImageTk.PhotoImage(imagen_redimensionada)
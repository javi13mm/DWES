from PIL import ImageTk, Image
from io import BytesIO
import requests

class Cell:
    def __init__(self, name, desc, url):
        self.name = name
        self.desc = desc
        self.url = url

        # imágenes accesibles desde clase Cell:
        response = requests.get(url)
        img_data = Image.open(BytesIO(response.content))
        self.img = ImageTk.PhotoImage(img_data)
        
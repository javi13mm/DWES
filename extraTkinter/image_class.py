from PIL import Image
from io import BytesIO
import requests

# Clase que guarda las imágenes como Objetos Image
class ImageClass:
    def __init__(self, url):
        response = requests.get(url)
        self.img = Image.open(BytesIO(response.content))
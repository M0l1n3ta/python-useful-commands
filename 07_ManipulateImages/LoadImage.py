# pip install Pillow

from PIL import Image
import os
from pathlib import Path

imageFilePath = os.path.join(os.getcwd(),'07_ManipulateImages/Resources/Sunflower.webp')


try:
    image = Image.open(imageFilePath)
    width, height = image.size
    print("Ancho :" ,width, "Alto: ",height)

    print(image.mode)

    print(image.format)

    image.show()
except FileNotFoundError as error:
    print('La imagen no existe')
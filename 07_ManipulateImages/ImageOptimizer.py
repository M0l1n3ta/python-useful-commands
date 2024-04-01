# Image Optimizing
# pip install Pillow
from PIL import Image,ImageFilter,ImageEnhance,ImageOps

from pathlib import Path

p = Path(__file__).with_name('FeriaAlbacete_2022.jpg')


# Croping 
im = Image.open(p)
im = im.crop((34, 23, 100, 100))
im.save(Path(__file__).with_name("Image1.jpg"))

# Resizing
im = Image.open(p)
im = im.resize((50, 50))
im.save(Path(__file__).with_name("Image2.jpg"))

# Flipping
im = Image.open(p)
im = im.transpose(Image.FLIP_LEFT_RIGHT)
im.save(Path(__file__).with_name("Image3.jpg"))

# Rotating
im = Image.open(p)
im = im.rotate(180)
im.save(Path(__file__).with_name("Image4.jpg"))

# Compressing
im = Image.open(p)
im.save(Path(__file__).with_name("FeriaAlbacete_2022_compress.jpg"), optimize=True, quality=90)


# Blurring
im = Image.open(p)
im = im.filter(ImageFilter.BLUR)
im.save(Path(__file__).with_name("Image5.jpg"))

# Sharpening
im = Image.open(p)
im = im.filter(ImageFilter.SHARPEN)
im.save(Path(__file__).with_name("Image6.jpg"))

# Set Brightness
im = Image.open(p)
im = ImageEnhance.Brightness(im)
im = im.enhance(1.5)
im.save(Path(__file__).with_name("Image7.jpg"))

# Set Contrast
im = Image.open(p)
im = ImageEnhance.Contrast(im)
im = im.enhance(1.5)
im.save(Path(__file__).with_name("Image8.jpg"))


# Adding Filters
im = Image.open(p)
im = ImageOps.grayscale(im)
im = ImageOps.invert(im)
im = ImageOps.posterize(im, 4)
im.save(Path(__file__).with_name("Image9.jpg"))
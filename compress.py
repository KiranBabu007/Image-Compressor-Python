from PIL import Image

height = 4410
width = 7680

img = Image.open('original.png')
img = img.resize((width, height), Image.ANTIALIAS)
img.save("resized.png")

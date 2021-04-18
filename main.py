from tgraphics import Texture#, Sprite, Screen
from PIL import Image
import numpy as np


img = Image.open("helloworld.gif")
img = img.convert("L")
img = img.resize((100, 100))
img = np.array(img)

img = img / np.max(img)

helloworld = img.tolist()

print(Texture(helloworld).distort_v(2))



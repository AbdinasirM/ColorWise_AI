
from rembg import remove
from PIL import Image


input = Image.open('C:/Users/Abdi/ColorWise_AI/Backend/imageProcessing/someone.jpg')

output = remove(input)

output.save('out.png')

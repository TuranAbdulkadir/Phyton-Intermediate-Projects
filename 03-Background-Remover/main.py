from rembg import remove
from PIL import Image

input_path = "input.jpg" # Put an image named input.jpg in folder
output_path = "output.png"

try:
    inp = Image.open(input_path)
    output = remove(inp)
    output.save(output_path)
    print("Background removed! Saved as output.png")
except:
    print("Error: Please put 'input.jpg' in this folder.")
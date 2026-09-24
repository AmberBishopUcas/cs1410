# Lab 1 image-editing demo.
# This script opens an image, applies a filter, and overlays a transparent PNG
# onto the original photo to create a composite image.
from PIL import Image
from helper_funcs import bw_rgb_filter, copy_paste

# Load the source image and the overlay to be pasted onto it.
bears = Image.open("C:\\Users\\11040991\\Documents\\Cs 1410 assingments\\images\\MV5BZDYxY2I1OGMtN2Y4MS00ZmU1LTgyNDAtODA0MzAyYjI0N2Y2XkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg")
baloon = Image.open("C:\\Users\\11040991\\Documents\\Cs 1410 assingments\\images\\baloon.png")

# Apply the custom filter to a copy so the original image remains unchanged.
bears_filtered = bears.copy()
bw_rgb_filter(bears_filtered)

# Overlay the balloon image at a chosen position on the original bear image.
copy_paste(baloon, bears, 100, 100)
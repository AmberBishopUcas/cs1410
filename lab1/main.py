from PIL import Image
from helper_funcs import bw_rgb_filter, copy_paste

bears = Image.open("C:\\Users\\11040991\\Documents\\Cs 1410 assingments\\images\\MV5BZDYxY2I1OGMtN2Y4MS00ZmU1LTgyNDAtODA0MzAyYjI0N2Y2XkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg")
baloon = Image.open("C:\\Users\\11040991\\Documents\\Cs 1410 assingments\\images\\baloon.png")


bears_filtered = bears.copy()
bw_rgb_filter(bears_filtered)


copy_paste(baloon, bears, 100, 100)
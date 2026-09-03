from PIL import Image
def bw_rgb_filter(img_object):
    pixel = img_object.load()
    width, height = img_object.size
    for i in range(height):
        for j in range(width):
            red, green, blue = pixel[j, i]
            brightness = int(0.299 * red + 0.587 * green + 0.114 * blue)   
            if brightness < 85:
                pixel[j, i] = (0, 0, 0)
            elif brightness > 170:
                pixel[j, i] = (255, 255, 255)
            else:
                if red > green and red > blue:
                    pixel[j, i] = (red, 0, 0)
                elif green > blue and green > red:
                    pixel[j, i] = (0, green, 0)
                else:
                    pixel[j, i] = (0, 0, blue)
    img_object.show()

    img_object.save("C:\\Users\\11040991\\Documents\\Cs 1410 assingments\\output\\bears2.jpg")

def copy_paste(copied_img, target_img, x, y):
    copied_pixel = copied_img.load()
    target_pixel = target_img.load()
    width, height = copied_img.size
    for i in range (height):
        for j in range (width):
            red, green, blue, alpha = copied_pixel[j, i]
            if alpha == 0:
                pass
            else:
                target_pixel[x + j, y + i] = (red, green, blue, alpha)
    target_img.show()
    target_img.save("C:\\Users\\11040991\\Documents\\Cs 1410 assingments\\output\\bears3.jpg")
    
if __name__ == "__main__":
    pass
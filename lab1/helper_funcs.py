# Image-processing helper functions for basic editing operations.
# These functions manipulate pixel values and overlay images to create a stylized result.
from PIL import Image


def bw_rgb_filter(img_object):
    """Convert the image into a high-contrast black/white and color-boosted effect."""
    pixel = img_object.load()
    width, height = img_object.size
    for i in range(height):
        for j in range(width):
            # read the color at each pixel and compute a brightness value
            red, green, blue = pixel[j, i]
            brightness = int(0.299 * red + 0.587 * green + 0.114 * blue)
            if brightness < 85:
                # dark pixels become black
                pixel[j, i] = (0, 0, 0)
            elif brightness > 170:
                # bright pixels become white
                pixel[j, i] = (255, 255, 255)
            else:
                # mid-tone pixels keep the dominant color channel to create a colored filter
                if red > green and red > blue:
                    pixel[j, i] = (red, 0, 0)
                elif green > blue and green > red:
                    pixel[j, i] = (0, green, 0)
                else:
                    pixel[j, i] = (0, 0, blue)
    img_object.show()

    # save the filtered result to the output folder so it can be reused later
    img_object.save("C:\\Users\\11040991\\Documents\\Cs 1410 assingments\\output\\bears2.jpg")


def copy_paste(copied_img, target_img, x, y):
    """Paste a transparent PNG onto a target image at a specific coordinate."""
    copied_pixel = copied_img.load()
    target_pixel = target_img.load()
    width, height = copied_img.size
    for i in range(height):
        for j in range(width):
            red, green, blue, alpha = copied_pixel[j, i]
            if alpha == 0:
                # transparent pixels are skipped so the background stays untouched
                pass
            else:
                # copy the visible pixel onto the destination image at the selected offset
                target_pixel[x + j, y + i] = (red, green, blue, alpha)
    target_img.show()
    target_img.save("C:\\Users\\11040991\\Documents\\Cs 1410 assingments\\output\\bears3.jpg")


if __name__ == "__main__":
    pass
from skimage.color import rgb2hsv
from skimage.color import hsv2rgb
import matplotlib.pyplot as plt
from skimage import io


def GreyExceptRed(image):
    hsv_img = rgb2hsv(image)
    for x in range(len(hsv_img[:, :, 0])):
        for y in range(len(hsv_img[:, :, 0][x])):
            if 0.1 < hsv_img[:, :, 0][x][y] < 0.9:
                hsv_img[:, :, 1][x][y] = 0.0

    histoFromImage(hsv_img)


def histoFromImage(plot_image):
    hue_img = plot_image[:, :, 0]

    fig, (histo, img) = plt.subplots(ncols=2, figsize=(8, 3))

    histo.hist(hue_img.ravel(), 50)
    histo.set_title("Histogram of the Hue channel")
    img.imshow(hsv2rgb(plot_image))
    img.set_title("Used image")
    plt.show()


image = io.imread('colorfull.jpg')

image_tmp = rgb2hsv(image)
histoFromImage(image_tmp)

GreyExceptRed(image)

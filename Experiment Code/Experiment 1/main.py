from skimage.viewer import ImageViewer
from skimage.color import rgb2hsv
from skimage import io

def FindTheEgg(image):
    hsv_img = rgb2hsv(image)
    for x in range(len(hsv_img[:, :, 0])):
        for y in range(len(hsv_img[:, :, 0][x])):
            if 0.1 < hsv_img[:, :, 0][x][y] > 0.3:
                image[x][y] = (0, 26, 143)
            else:
                image[x][y] = (128, 0, 5)

    viewer = ImageViewer(image)
    viewer.show()


egg1 = io.imread('egg_one.jpg')
egg2 = io.imread('egg_two.jpg')
egg3 = io.imread('egg_three.jpg')
FindTheEgg(egg1)
FindTheEgg(egg2)
FindTheEgg(egg3)

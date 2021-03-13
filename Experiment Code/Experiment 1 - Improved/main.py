from skimage.viewer import ImageViewer
from skimage.transform import resize
from skimage import io
import numpy as np


def saveAndShowImage(image, name):
    viewer = ImageViewer(image)
    viewer.show()
    io.imsave(name+".jpg", image)


def SimplifyEggs(image):
    image = resize(image, (image.shape[0] // 4, image.shape[1] // 4), anti_aliasing=True)

    for row in range(len(image)):
        for pixel in range(len(image[row])):
            for i in range(3):
                image[row][pixel][i] = int(image[row][pixel][i] * 255)

            if image[row][pixel][0] == 0:
                image[row][pixel][0] = 1
            if int(image[row][pixel][1]) + int(image[row][pixel][2]) == 0:
                image[row][pixel][1] = 1

            red_percentage = (image[row][pixel][0] / (int(image[row][pixel][1]) + int(image[row][pixel][2]))) * 100

            if red_percentage < 140:
                image[row][pixel] = [0, 255, 255]
            else:
                image[row][pixel] = [0, 0, 0]

    image = resize(image, (image.shape[0] * 4, image.shape[1] * 4), anti_aliasing=True)
    image = image.astype(np.uint8)
    return image


egg1 = io.imread('egg1.jpg')
egg2 = io.imread('egg2.jpg')
egg3 = io.imread('egg3.jpg')

saveAndShowImage( SimplifyEggs(egg1), "egg1_Result" )
saveAndShowImage( SimplifyEggs(egg2), "egg2_Result" )
saveAndShowImage( SimplifyEggs(egg3), "egg3_Result" )


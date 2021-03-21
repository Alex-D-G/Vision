from skimage.transform import resize
from skimage import io
import numpy as np


def SimplifyEggs(image):
    size_multiplier = 4
    image = resize(image, (image.shape[0] // size_multiplier, image.shape[1] // size_multiplier), anti_aliasing=True)

    for row in range(len(image)):
        for pixel in range(len(image[row])):
            for i in range(3):
                image[row][pixel][i] = int(image[row][pixel][i] * 255)

            if image[row][pixel][0] == 0:
                image[row][pixel][0] = 1
            if int(image[row][pixel][1]) + int(image[row][pixel][2]) == 0:
                image[row][pixel][1] = 1

            red_percentage = (image[row][pixel][0] / (int(image[row][pixel][1]) + int(image[row][pixel][2]))) * 100

            if red_percentage < 110:
                image[row][pixel] = [0, 255, 255]
            else:
                image[row][pixel] = [0, 0, 0]

    image = resize(image, (image.shape[0] * size_multiplier, image.shape[1] * size_multiplier), anti_aliasing=True)
    image = image.astype(np.uint8)
    return image


def convert_eggs(location):
    egg_images = io.imread_collection(location)

    for i, egg in enumerate(egg_images):
        io.imsave("result_"+ str(i) + ".jpg", SimplifyEggs(egg))


convert_eggs('to_convert/*.jpg')

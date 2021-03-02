from skimage import data
from skimage import transform
import numpy as np
import matplotlib.pyplot as plt

image = data.camera()

matrix_move = np.array([[1, 0, 30], [0, 1, 30], [0, 0, 1]])
new_size = (image.shape[0], image.shape[1]*2)

tf_rotate = transform.SimilarityTransform(rotation=np.deg2rad(10))
tf_move = transform.SimilarityTransform(matrix_move)

after_image = transform.warp(image, tf_rotate)
after_image = transform.warp(after_image, tf_move)
after_image = transform.resize(after_image, new_size)


def show2Images(image1, image2):

    fig, (img1, img2) = plt.subplots(ncols=2, figsize=(8, 3))

    img1.imshow(image1)
    img1.set_title("before image")

    img2.imshow(image2)
    img2.set_title("after image")
    plt.show()


show2Images(image, after_image)

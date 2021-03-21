from skimage.viewer import ImageViewer
from skimage.color import rgb2gray
from skimage.transform import resize
from skimage import io


def load_train():
    train_images = io.imread_collection('train_data/*.jpg')
    labels = [ 1, 4, 6, 3, 6, 2, 9, 6, 3]
    return train_images, labels


def prepare_image_list(images, decrease):
    converted_list = []
    for image in images:
        gray_image = rgb2gray(image)
        converted_image = resize(gray_image, (gray_image.shape[0] // decrease, gray_image.shape[1] // decrease))
        converted_list.append(converted_image)

    return converted_list


def prepare_image(image, decrease):
    gray_image = rgb2gray(image)
    converted_image = resize(gray_image, (gray_image.shape[0] // decrease, gray_image.shape[1] // decrease))

    return converted_image


def average_egg_size(images, labels):
    images = prepare_image_list(images, 4)
    average_total = 0
    for i, image in enumerate(images):
        average_image = 0

        for row in image:
            for pixel in row:
                if pixel != 0:

                    average_image += 1

        average_image /= labels[i]
        average_total += average_image

    return average_total / len(images)


def find_eggs(image, average):
    image = prepare_image(image, 4)
    pixel_count = 0
    for row in image:
        for pixel in row:
            if pixel != 0:
                pixel_count += 1

    return round(pixel_count / average)


test_images = io.imread_collection('test_data/*.jpg')
train_images, train_labels = load_train()

average_egg = average_egg_size(train_images, train_labels)

for test_image in test_images:
    print(find_eggs(test_image, average_egg))
    viewer = ImageViewer(test_image)
    viewer.show()

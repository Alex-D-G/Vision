from skimage.viewer import ImageViewer
from skimage import data, filters
from skimage import feature
from scipy import ndimage
import scipy

image = data.camera()
viewer = ImageViewer(image)
viewer.show()

#Edge self 1
mask1 = [[-1/9, 1/9]]

newImage = scipy.ndimage.convolve(image, mask1)
newImage = scipy.ndimage.convolve(newImage, mask1)

viewer = ImageViewer(newImage)
viewer.show()

#Edge self 2
mask1 = [
           [-1/9, 0/9, 1/9],
           [-1/9, 0/9, 1/9],
           [-1/9, 0/9, 1/9]
        ]

newImage = scipy.ndimage.convolve(image, mask1)
newImage = scipy.ndimage.convolve(newImage, mask1)

viewer = ImageViewer(newImage)
viewer.show()

#Edge self 3
mask1 = [
           [-1/9, -3/9, 1/9],
           [0/9, 0/9, 0/9],
           [1/9, 3/9, 1/9]
        ]

newImage = scipy.ndimage.convolve(image, mask1)
newImage = scipy.ndimage.convolve(newImage, mask1)

viewer = ImageViewer(newImage)
viewer.show()

#Edge skimage 1
edges = filters.prewitt(image)

viewer = ImageViewer(edges)
viewer.show()

#Edge skimage 2
edges = filters.sobel(image)

viewer = ImageViewer(edges)
viewer.show()

#Edge skimage 3
edges = filters.roberts(image)

viewer = ImageViewer(edges)
viewer.show()

#De Filters van Skimage zijn een stuk beter, ze zijn makkelijker te gebruiken en werker ook beter

#Canny Edge

edges = feature.canny(image, sigma=2.5)

viewer = ImageViewer(edges)
viewer.show()

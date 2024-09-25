from skimage.transform import resize
from skimage.filters import gaussian, sobel
from skimage.transform import rotate

def resize_image(image, proportion):
    assert 0 <= proportion <= 1, "Specify a valid proportion between 0 and 1."
    height = round(image.shape[0] * proportion)
    width = round(image.shape[1] * proportion)
    image_resized = resize(image, (height, width), anti_aliasing=True)
    return image_resized

def apply_gaussian_filter(image, sigma=1):
    return gaussian(image, sigma=sigma, multichannel=True)

def apply_sobel_filter(image):
    return sobel(image)

from skimage.transform import rotate

def rotate_image(image, angle):
    return rotate(image, angle)

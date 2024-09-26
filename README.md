# Image Processing Packages

Description. 
The package *processamento-imagens-matheus* is used for:
- Processing:
  	- Transfer histogram between two images.
  	- Find differences between two images based on structural similarity 	index (SSIM).
  	- Resize images with specified proportions.
 	- Apply Gaussian and Sobel filters for smoothing and edge detection.
  	- Rotate images by a specified angle.
- Utilities:
  - Read and save images.
  - Plot images, comparison results, and histograms (grayscale or RGB).

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install *processamento-imagens-matheus*

```bash
pip install processamento-imagens-matheus
```

## Usage

```python
from processing.combination import transfer_histogram, find_difference
from processing.transformation import resize_image, apply_gaussian_filter, apply_sobel_filter, rotate_image
from utils.io import read_image, save_image
from utils.plot import plot_image, plot_result, plot_histogram

# Transfer histogram between two images
image1 = read_image('path_to_image1.jpg')
image2 = read_image('path_to_image2.jpg')

matched_image = transfer_histogram(image1, image2)
plot_result(image1, image2, matched_image)

# Resize an image
resized_image = resize_image(image1, 0.5)
plot_image(resized_image)

# Apply Sobel filter
edges_image = apply_sobel_filter(image1)
plot_image(edges_image)
```

## Author
Matheus Pizani

## License
[MIT](https://choosealicense.com/licenses/mit/)
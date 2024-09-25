import matplotlib.pyplot as plt

def plot_image(image):
    plt.figure(figsize=(12, 4))
    plt.imshow(image, cmap='gray')
    plt.axis('off')
    plt.show()

def plot_result(*args):
    number_images = len(args)
    fig, axis = plt.subplots(nrows=1, ncols = number_images, figsize=(12, 4))
    names_lst = ['Image {}'.format(i) for i in range(1, number_images)]
    names_lst.append('Result')
    for ax, name, image in zip(axis, names_lst, args):
        ax.set_title(name)
        ax.imshow(image, cmap='gray')
        ax.axis('off')
    fig.tight_layout()
    plt.show()

def plot_histogram(image):
    if len(image.shape) == 2:  # Verifica se a imagem é em escala de cinza
        plt.figure(figsize=(6, 4))
        plt.hist(image.ravel(), bins=256, color='black', alpha=0.8)
        plt.title('Grayscale Histogram')
        plt.tight_layout()
        plt.show()
    elif len(image.shape) == 3:  # Verifica se a imagem é colorida (RGB)
        fig, axis = plt.subplots(nrows=1, ncols=3, figsize=(12, 4), sharex=True, sharey=True)
        color_lst = ['red', 'green', 'blue']
        for index, (ax, color) in enumerate(zip(axis, color_lst)):
            ax.set_title('{} histogram'.format(color.title()))
            ax.hist(image[:, :, index].ravel(), bins=256, color=color, alpha=0.8)
        fig.tight_layout()
        plt.show()
    else:
        raise ValueError("Image format not supported for histogram plotting.")

"""This example shows how to mask an image with opencv
"""
import cv2
import numpy as np
from context import pendulum
from pendulum.io import load_image, save_image
from pendulum.image_processing import mask
import matplotlib.pyplot as plt

def main():
    # Load an image
    image = load_image('examples/data/test.jpg')
    # Define the corners of the mask
    corners = np.array([[500, 300], [2950, 200], 
                        [3100, 2000], [500, 2100]])
    # Mask the image
    masked_image, pmask = mask(image, corners)
    plt.imshow(masked_image, cmap='gray')
    plt.show()

    return

if __name__ == '__main__':
    main()
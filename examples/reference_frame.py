"""Define a reference frame for the image from the reference points drawn in green.
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
from context import pendulum
from pendulum.io import load_image, save_image
from pendulum.image_processing import mask, mask_by_color



def main():

    # Load an image
    image = load_image('examples/data/test.jpg')
    # Define the corners of the mask
    corners = np.array([[500, 300], [2950, 200], 
                        [3100, 2000], [500, 2100]])
    # Mask the image
    masked_image, pmask = mask(image, corners)

    # Define the color range for the green color
    lower_green = np.array([70, 40, 40])
    upper_green = np.array([90, 255, 255])
    # Mask the image by color
    green_regions = mask_by_color(masked_image, lower_green, upper_green, cv2.COLOR_RGB2HSV)
    plt.imshow(green_regions, cmap='gray')
    plt.show()
    return

if __name__ == '__main__':
    main()
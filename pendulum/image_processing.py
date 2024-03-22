import numpy as np
import cv2

def mask(image, corners):
    """Mask an image with opencv

    Args:
        image (array): an image in numpy array format
        corners (array): an array with all the corners (x,y) around which to apply the mask 

    Returns:
        array: the masked image
        array: the mask
    """    
    mask = np.zeros(image.shape[:2], dtype=np.uint8)
    # then mask the region outside of these four corners
    mask_corners = np.array(corners)
    cv2.drawContours(mask, [mask_corners], -1, 255, -1)
    masked_image = cv2.bitwise_and(image, image, mask=mask)
    return masked_image, mask

def mask_by_color(image, lower_bound, upper_bound, color_conversion=cv2.COLOR_BGR2HSV):
    """Mask an image by color with opencv

    Args:
        image (array): an image in numpy array format
        lower_bound (array): the lower bound of the color range
        upper_bound (array): the upper bound of the color range

    Returns:
        array: the mask
    """
    hsv_image = cv2.cvtColor(image, color_conversion)
    mask = cv2.inRange(hsv_image, lower_bound, upper_bound)
    return mask
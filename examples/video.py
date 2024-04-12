"""This example shows how to acquire a video and extract frames from it
"""
import cv2
import numpy as np
from context import pendulum
from pendulum.io import video_capture
#from pendulum.image_processing import mask
import matplotlib.pyplot as plt

def main():
    # Load an image
    video = video_capture('examples/data/test_video')
    
    #plt.imshow(masked_image, cmap='gray')
    #plt.show()

    return

if __name__ == '__main__':
    main()
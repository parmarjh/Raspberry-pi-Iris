import cv2
import numpy as np
import matplotlib.pyplot as plt

def show_image_in_graph(img):
    ax = plt.subplot()
    ax.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.show()

image = cv2.imread('Denoised_real.jpg')

show_image_in_graph(image)

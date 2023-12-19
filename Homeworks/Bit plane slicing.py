import cv2
import numpy as np
import matplotlib.pyplot as plt

def bit_plane_slice(image_path, bit_level):

    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)


    bit_plane = (image >> bit_level) & 1


    plt.imshow(bit_plane, cmap='gray')
    plt.title(f'Bit Plane {bit_level}')
    plt.axis('off')
    plt.show()


image_path = 'path/to/your/image.jpg'
bit_level = 7


bit_plane_slice(image_path, bit_level)

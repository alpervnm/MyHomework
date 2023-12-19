import cv2
import numpy as np
import matplotlib.pyplot as plt

def gaussian_filter(image_path, kernel_size):
    # Görüntüyü oku
    image = cv2.imread(image_path)

    # OpenCV, görüntüyü BGR formatında okur, gri tonlamalıya dönüştür
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Gaussian filtresi uygula
    blurred_image = cv2.GaussianBlur(gray_image, (kernel_size, kernel_size), 0)

    # Görüntüleri görselleştir
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(gray_image, cmap='gray')
    plt.title('Orijinal Gri Tonlamalı Görüntü')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(blurred_image, cmap='gray')
    plt.title(f'Gaussian Filtre (Kernel Boyutu: {kernel_size})')
    plt.axis('off')

    plt.show()

# Örnek olarak bir görüntü dosyası ve kernel boyutunu belirtin
image_path = 'path/to/your/image.jpg'
kernel_size = 5  # Kernel boyutu (tek sayı olmalı)

# Gaussian filtresi fonksiyonunu çağır
gaussian_filter(image_path, kernel_size)

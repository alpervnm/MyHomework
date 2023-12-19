import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_laplacian_blur(image_path, kernel_size):
    # Görüntüyü oku
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Blurring operasyonu (örneğin, Gaussian filtresi)
    blurred_image = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)

    # Laplace operatörü uygula
    laplacian = cv2.Laplacian(blurred_image, cv2.CV_64F)

    # Görüntüleri görselleştir
    plt.figure(figsize=(12, 4))

    plt.subplot(1, 3, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Orijinal Gri Tonlamalı Görüntü')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(blurred_image, cmap='gray')
    plt.title('Blurring (Gaussian Filtresi)')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(laplacian, cmap='gray')
    plt.title('Laplace Operatörü Sonucu')
    plt.axis('off')

    plt.show()

# Örnek olarak bir görüntü dosyası ve kernel boyutunu belirtin
image_path = 'path/to/your/image.jpg'
kernel_size = 5  # Kernel boyutu (tek sayı olmalı)

# Laplace operatörü ve blurring fonksiyonunu çağır
apply_laplacian_blur(image_path, kernel_size)

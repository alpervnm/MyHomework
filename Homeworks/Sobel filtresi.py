import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_sobel_filter(image_path):
    # Görüntüyü oku
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Sobel filtresi uygula
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

    # Sobel gradyanlarından kenar büyüklüğünü hesapla
    gradient_magnitude = np.sqrt(sobel_x**2 + sobel_y**2)

    # Görüntüleri görselleştir
    plt.figure(figsize=(12, 4))

    plt.subplot(1, 3, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Orijinal Gri Tonlamalı Görüntü')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(np.abs(sobel_x), cmap='gray')
    plt.title('Sobel Filtresi (X Yönü)')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(gradient_magnitude, cmap='gray')
    plt.title('Kenar Büyüklüğü (Sobel Filtresi)')
    plt.axis('off')

    plt.show()

# Örnek olarak bir görüntü dosyası belirtin
image_path = 'path/to/your/image.jpg'

# Sobel filtresi fonksiyonunu çağır
apply_sobel_filter(image_path)

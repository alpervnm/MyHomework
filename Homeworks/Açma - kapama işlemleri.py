import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_opening_closing(image_path, kernel_size_opening, kernel_size_closing):
    # Görüntüyü oku
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Yapılandırma elemanını oluştur
    kernel_opening = np.ones((kernel_size_opening, kernel_size_opening), np.uint8)
    kernel_closing = np.ones((kernel_size_closing, kernel_size_closing), np.uint8)

    # Açma işlemi uygula
    opened_image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel_opening)

    # Kapatma işlemi uygula
    closed_image = cv2.morphologyEx(opened_image, cv2.MORPH_CLOSE, kernel_closing)

    # Görüntüleri görselleştir
    plt.figure(figsize=(12, 4))

    plt.subplot(1, 3, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Orijinal Görüntü')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(opened_image, cmap='gray')
    plt.title(f'Açma (Kernel Boyutu: {kernel_size_opening})')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(closed_image, cmap='gray')
    plt.title(f'Kapatma (Kernel Boyutu: {kernel_size_closing})')
    plt.axis('off')

    plt.show()

# Örnek olarak bir görüntü dosyası ve kernel boyutlarını belirtin
image_path = 'path/to/your/image.jpg'
kernel_size_opening = 5  # Açma işlemi için kernel boyutu
kernel_size_closing = 5  # Kapatma işlemi için kernel boyutu

# Açma ve kapatma işlemlerini uygula
apply_opening_closing(image_path, kernel_size_opening, kernel_size_closing)

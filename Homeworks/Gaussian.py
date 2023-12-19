import cv2
import matplotlib.pyplot as plt

def apply_gaussian_filter(image_path, kernel_size):
    # Görüntüyü oku
    image = cv2.imread(image_path)

    # Gaussian filtresi uygula
    blurred_image = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)

    # Görüntüleri görselleştir
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(image[:, :, ::-1])
    plt.title('Orijinal Görüntü')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(blurred_image[:, :, ::-1])
    plt.title(f'Gaussian Filtre (Kernel Boyutu: {kernel_size})')
    plt.axis('off')

    plt.show()

# Örnek olarak bir görüntü dosyası ve kernel boyutunu belirtin
image_path = 'path/to/your/image.jpg'
kernel_size = 5  # Kernel boyutu (tek sayı olmalı)

# Gaussian filtresi fonksiyonunu çağır
apply_gaussian_filter(image_path, kernel_size)

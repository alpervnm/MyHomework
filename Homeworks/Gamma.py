import cv2
import numpy as np
import matplotlib.pyplot as plt

def gamma_correction(image_path, gamma):
    # Görüntüyü oku
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Gamma düzeltme işlemi
    corrected_image = np.power(image/float(np.max(image)), gamma) * 255.0

    # Görüntüleri görselleştir
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Orijinal Görüntü')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(corrected_image, cmap='gray')
    plt.title(f'Gamma Düzeltme (Gamma={gamma})')
    plt.axis('off')

    plt.show()

# Örnek olarak bir görüntü dosyası ve gamma değerini belirtin
image_path = 'path/to/your/image.jpg'
gamma_value = 1.5  # Gamma değeri

# Gamma düzeltme fonksiyonunu çağır
gamma_correction(image_path, gamma_value)

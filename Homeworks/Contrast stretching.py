import cv2
import numpy as np
import matplotlib.pyplot as plt

def contrast_stretching(image_path, lower_limit, upper_limit):
    # Görüntüyü oku
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Kontrast germe işlemi
    stretched_image = cv2.normalize(image, None, alpha=lower_limit, beta=upper_limit, norm_type=cv2.NORM_MINMAX)

    # Görüntüleri görselleştir
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Orijinal Görüntü')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(stretched_image, cmap='gray')
    plt.title('Kontrast Gerilmiş Görüntü')
    plt.axis('off')

    plt.show()

# Örnek olarak bir görüntü dosyası ve kontrast germe aralığını belirtin
image_path = 'path/to/your/image.jpg'
lower_limit = 0.2  # Alt sınır
upper_limit = 0.8  # Üst sınır

# Kontrast germe fonksiyonunu çağır
contrast_stretching(image_path, lower_limit, upper_limit)

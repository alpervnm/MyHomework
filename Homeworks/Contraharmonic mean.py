import cv2
import numpy as np
import matplotlib.pyplot as plt

def contraharmonic_mean_filter(image_path, window_size, Q):
    # Görüntüyü oku
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Görüntü boyutları
    rows, cols = image.shape

    # Filtrelenmiş görüntüyü saklamak için bir dizi oluştur
    filtered_image = np.zeros_like(image, dtype=np.float32)

    # Filtreleme işlemi
    for i in range(rows - window_size + 1):
        for j in range(cols - window_size + 1):
            window = image[i:i+window_size, j:j+window_size].astype(np.float32)
            numerator = np.sum(np.power(window, Q+1))
            denominator = np.sum(np.power(window, Q))
            filtered_image[i, j] = numerator / max(denominator, 1e-10)

    # Görüntüleri görselleştir
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Orijinal Görüntü')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(filtered_image, cmap='gray')
    plt.title(f'Contraharmonic Mean Filtresi (Q={Q}, Window Size={window_size})')
    plt.axis('off')

    plt.show()

# Örnek olarak bir görüntü dosyası, pencere boyutu ve Q faktörünü belirtin
image_path = 'path/to/your/image.jpg'
window_size = 3  # Pencere boyutu (tek sayı olmalı)
Q = 1.5  # Q faktörü

# Contraharmonic Mean filtresi fonksiyonunu çağır
contraharmonic_mean_filter(image_path, window_size, Q)

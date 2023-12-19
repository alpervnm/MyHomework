import cv2
import matplotlib.pyplot as plt

def histogram_equalization(image_path):
    # Görüntüyü oku
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Histogram eşitleme işlemi
    equalized_image = cv2.equalizeHist(image)

    # Görüntüleri görselleştir
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Orijinal Görüntü')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(equalized_image, cmap='gray')
    plt.title('Histogram Eşitlenmiş Görüntü')
    plt.axis('off')

    plt.show()

# Örnek olarak bir görüntü dosyası belirtin
image_path = 'path/to/your/image.jpg'

# Histogram eşitleme fonksiyonunu çağır
histogram_equalization(image_path)
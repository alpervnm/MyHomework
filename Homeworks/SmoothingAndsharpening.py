import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_smoothing_and_sharpening(image_path, smoothing_kernel_size, sharpening_strength):
    # Görüntüyü oku
    image = cv2.imread(image_path)

    # Smoothing (Bulanıklık) işlemi (örneğin, Gaussian filtresi)
    smoothed_image = cv2.GaussianBlur(image, (smoothing_kernel_size, smoothing_kernel_size), 0)

    # Sharpening (Keskinleştirme) işlemi (örneğin, unsharp masking)
    sharpened_image = cv2.addWeighted(image, 1 + sharpening_strength, smoothed_image, -sharpening_strength, 0)

    # Görüntüleri görselleştir
    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    plt.imshow(image[:, :, ::-1])
    plt.title('Orijinal Görüntü')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(smoothed_image[:, :, ::-1])
    plt.title(f'Smoothing (Kernel Boyutu: {smoothing_kernel_size})')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(sharpened_image[:, :, ::-1])
    plt.title(f'Sharpening (Güç: {sharpening_strength})')
    plt.axis('off')

    plt.show()

# Örnek olarak bir görüntü dosyası, smoothing kernel boyutu ve sharpening gücünü belirtin
image_path = 'path/to/your/image.jpg'
smoothing_kernel_size = 5  # Smoothing (bulanıklık) için kernel boyutu
sharpening_strength = 1.5  # Sharpening (keskinleştirme) gücü

# Smoothing ve sharpening fonksiyonunu çağır
apply_smoothing_and_sharpening(image_path, smoothing_kernel_size, sharpening_strength)

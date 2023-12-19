import cv2
import numpy as np
import matplotlib.pyplot as plt

def add_salt_and_pepper_noise(image, salt_prob, pepper_prob):
    noisy_image = np.copy(image)

    # Salt gürültüsü ekle
    salt_pixels = np.random.random(image.shape[:2]) < salt_prob
    noisy_image[salt_pixels] = 255

    # Pepper gürültüsü ekle
    pepper_pixels = np.random.random(image.shape[:2]) < pepper_prob
    noisy_image[pepper_pixels] = 0

    return noisy_image

def remove_salt_and_pepper_noise(image, kernel_size):
    cleaned_image = cv2.medianBlur(image, kernel_size)
    return cleaned_image

# Örnek olarak bir görüntü dosyası ve gürültü olasılıklarını belirtin
image_path = 'path/to/your/image.jpg'
salt_probability = 0.02  # Salt gürültü olasılığı
pepper_probability = 0.02  # Pepper gürültü olasılığı

# Görüntüyü oku
original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Salt-and-pepper gürültüsü ekle
noisy_image = add_salt_and_pepper_noise(original_image, salt_probability, pepper_probability)

# Salt-and-pepper gürültüsü temizle
cleaned_image = remove_salt_and_pepper_noise(noisy_image, kernel_size=3)

# Görüntüleri görselleştir
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.imshow(original_image, cmap='gray')
plt.title('Orijinal Görüntü')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(noisy_image, cmap='gray')
plt.title('Salt-and-Pepper Gürültülü Görüntü')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(cleaned_image, cmap='gray')
plt.title('Temizlenmiş Görüntü')
plt.axis('off')

plt.show()

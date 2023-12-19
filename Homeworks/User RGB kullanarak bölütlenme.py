import cv2
import numpy as np
import matplotlib.pyplot as plt

def color_channel_segmentation(image_path, channel_index):
    # Görüntüyü oku
    image = cv2.imread(image_path)

    # Renk kanallarını ayır
    b, g, r = cv2.split(image)

    # Sadece seçilen renk kanalını vurgula
    segmented_channel = np.zeros_like(image)
    segmented_channel[:, :, channel_index] = image[:, :, channel_index]

    # Görüntüleri görselleştir
    plt.figure(figsize=(12, 4))

    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Orijinal Görüntü')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(segmented_channel)
    plt.title(f'{["Mavi", "Yeşil", "Kırmızı"][channel_index]} Kanalı Vurgulanmış Görüntü')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB) - segmented_channel)
    plt.title('Diğer Renk Kanalları')
    plt.axis('off')

    plt.show()

# Örnek olarak bir görüntü dosyası ve vurgulanacak renk kanalını belirtin
image_path = 'path/to/your/image.jpg'
channel_index_to_highlight = 1  # 0: Mavi, 1: Yeşil, 2: Kırmızı

# Renk kanalı bölütlenme fonksiyonunu çağır
color_channel_segmentation(image_path, channel_index_to_highlight)

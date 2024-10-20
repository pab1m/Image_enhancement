import cv2
import numpy as np
from matplotlib import pyplot as plt


def unsharp_masking(image, kernel_size=(5, 5), sigma=1.0, amount=1.5, threshold=0):
    # Створення Гауссового розмитого зображення
    blurred = cv2.GaussianBlur(image, kernel_size, sigma)

    # Обчислення різниці між оригіналом і розмитим зображенням
    mask = cv2.addWeighted(image, 1 + amount, blurred, -amount, 0)

    # Порогова обробка маски для видалення незначних змін
    low_contrast_mask = np.abs(image - blurred) < threshold
    np.copyto(mask, image, where=low_contrast_mask)

    return mask

image = cv2.imread('img/img5.png', cv2.IMREAD_GRAYSCALE)

# Застосування методу маскування непрямого підсилення
sharpened_image = unsharp_masking(image)

# Відображення оригінального та обробленого зображення
plt.figure(figsize=(13, 6))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Unsharp Masked Image')
plt.imshow(sharpened_image, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()

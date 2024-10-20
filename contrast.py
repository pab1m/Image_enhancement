import cv2
from matplotlib import pyplot as plt


def adjust_brightness_contrast(image, alpha, beta):
    adjusted = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    return adjusted

# Завантаження зображення
image = cv2.imread('img/img6.JPG')

# Налаштування яскравості та контрасту
alpha = 1.5  # Збільшення контрасту
beta = 50    # Збільшення яскравості
adjusted_image = adjust_brightness_contrast(image, alpha, beta)

# Відображення зображення
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Контраст та яскравість')
plt.imshow(cv2.cvtColor(adjusted_image, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.tight_layout()
plt.show()

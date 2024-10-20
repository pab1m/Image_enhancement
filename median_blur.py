import cv2
import matplotlib.pyplot as plt


# Завантаження зображення
image = cv2.imread('img/img2.png', cv2.IMREAD_GRAYSCALE)

# Застосування медіанного фільтра
median_blur = cv2.medianBlur(image, 5)

plt.figure(figsize=(12, 6))

# Відображення результату
plt.subplot(2, 1, 1), plt.imshow(image, cmap='gray'), plt.title('Оригінал')
plt.subplot(2, 1, 2), plt.imshow(median_blur, cmap='gray'), plt.title('Медіанний фільтр')
plt.show()

import cv2
import matplotlib.pyplot as plt


# Завантаження зображення
image = cv2.imread('img/img1.jpg', cv2.IMREAD_GRAYSCALE)

# Застосування Гауссового фільтра
gaussian_blur = cv2.GaussianBlur(image, (5, 5), 0)

plt.figure(figsize=(12, 6))

# Відображення результату
plt.subplot(1, 2, 1), plt.imshow(image, cmap='gray'), plt.title('Оригінал')
plt.subplot(1, 2, 2), plt.imshow(gaussian_blur, cmap='gray'), plt.title('Гауссовий фільтр')
plt.show()


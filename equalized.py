import cv2
import matplotlib.pyplot as plt


# Завантаження зображення
image = cv2.imread('img/img4.png', cv2.IMREAD_GRAYSCALE)

# Гістограмне вирівнювання
equalized = cv2.equalizeHist(image)

# Відображення результату
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1), plt.imshow(image, cmap='gray'), plt.title('Оригінал')
plt.subplot(1, 2, 2), plt.imshow(equalized, cmap='gray'), plt.title('Гістограмне вирівнювання')
plt.show()

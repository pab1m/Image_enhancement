import cv2
import matplotlib.pyplot as plt


# Завантаження зображення
image = cv2.imread('img/img3.jpg', cv2.IMREAD_GRAYSCALE)

# Застосування оператора Собеля
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
sobel = cv2.magnitude(sobel_x, sobel_y)

# Нормалізація результатів оператора Собеля для більшої виразності
sobel_x = cv2.normalize(sobel_x, None, 0, 255, cv2.NORM_MINMAX)
sobel_y = cv2.normalize(sobel_y, None, 0, 255, cv2.NORM_MINMAX)
sobel = cv2.normalize(sobel, None, 0, 255, cv2.NORM_MINMAX)

# Перетворення типів даних зображення для відображення
sobel_x = sobel_x.astype('uint8')
sobel_y = sobel_y.astype('uint8')
sobel = sobel.astype('uint8')

# Налаштування фігури для відображення
plt.figure(figsize=(18, 6))  # Встановлення більшого розміру фігури

# Відображення результату
plt.subplot(1, 4, 1), plt.imshow(image, cmap='gray'), plt.title('Оригінал')
plt.subplot(1, 4, 2), plt.imshow(sobel_x, cmap='gray'), plt.title('Собель X')
plt.subplot(1, 4, 3), plt.imshow(sobel_y, cmap='gray'), plt.title('Собель Y')
plt.subplot(1, 4, 4), plt.imshow(sobel, cmap='gray'), plt.title('Магнітуда Собеля')

# Налаштування відстані між зображеннями
plt.subplots_adjust(wspace=0.2)  # Збільшення відстані між підграфіками

plt.show()

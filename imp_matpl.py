import matplotlib.pyplot as plt
import numpy as np
# plt.plot([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6])
# plt.show()

# Незалежна (x) и залежна (y) змінні
x = np.linspace(0, 10, 50)
y1 = x
# Побудова графіка
# plt.title('Лінійна залежність y = x')  # заголовок
# plt.xlabel('x')  # вісь абсцис
# plt.ylabel('y')  # вісь ординат
# plt.grid()  # включення відображення сітки
# plt.plot(x, y, 'r--')  # побудова графіка
# plt.show()

# Квадратична залежність
y2 = [i**2 for i in x]
# Построение графика
plt.title('Залежності: y1 = x, y2 = x^2')  # заголовок
plt.xlabel('x')  # вісь абсцис
plt.ylabel('y1, y2')  # вісь ординат
plt.grid()  # включення відображення сітки
plt.plot(x, y1, x, y2)  # # побудова графіка
plt.show()

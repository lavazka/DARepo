import matplotlib.pyplot as plt
import numpy as np
# plt.plot([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6])
# plt.show()

# Независимая (x) и зависимая (y) переменные
x = np.linspace(0, 10, 50)
y1 = x
# Построение графика
# plt.title('Линейная зависимость y = x')  # заголовок
# plt.xlabel('x')  # ось абсцисс
# plt.ylabel('y')  # ось ординат
# plt.grid()  # включение отображения сетки
# plt.plot(x, y, 'r--')  # построение графика
# plt.show()

# Квадратичная зависимость
y2 = [i**2 for i in x]
# Построение графика
plt.title('Зависимости: y1 = x, y2 = x^2')  # заголовок
plt.xlabel('x')  # ось абсцисс
plt.ylabel('y1, y2')  # ось ординат
plt.grid()  # включение отображения сетки
plt.plot(x, y1, x, y2)  # построение графика
plt.show()

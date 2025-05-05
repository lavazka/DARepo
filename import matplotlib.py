import matplotlib.pyplot as plt
import numpy as np
# plt.plot([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6])
plt.show()

# Независимая (x) и зависимая (y) переменные
x = np.linspace(0, 10, 50)
y = x
# Построение графика
plt.title('Линейная зависимость y = x')  # заголовок
plt.xlabel('x')  # ось абсцисс
plt.ylabel('y')  # ось ординат
plt.grid()  # включение отображения сетки
plt.plot(x, y)  # построение графика

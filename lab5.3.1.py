import numpy as np
import matplotlib.pyplot as plt

a_values = np.arange(-5, 12, 0.5)
x = 3.567
y_values = (np.tan(a_values)**3) + (2.24 * x * a_values)

max_val = np.max(y_values)
min_val = np.min(y_values)
mean_val = np.mean(y_values)

print('Список аргументов функции: ', a_values)
print('Список значений функции: ', y_values)

print("Максимальное значение: ", max_val)
print('Минимальное значение: ', min_val)
print('Среднее значение: ', mean_val)

count = len(y_values)
sorted_vals = np.sort(y_values)
print('Отсортированный по возростанию значения функции f(x): ', sorted_vals)

# построение графика
plt.plot(a_values, y_values, label='f(x)')
mean_line = np.full_like(a_values, mean_val)
plt.plot(a_values, mean_line, label='mean val')
plt.legend(loc='lower right')
plt.xlabel('x')
plt.ylabel('y')
plt.title("График функции f(x) + график среднего значения")
plt.grid(True)
plt.show()

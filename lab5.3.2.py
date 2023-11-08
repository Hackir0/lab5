import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-8, 8, 80)
y = np.linspace(-8, 8, 80)

X, Y = np.meshgrid(x, y)

X = np.where(X < 0, 0, X)
Y = np.where(Y < 0, 0, Y)

Z1 = X ** 0.25 + Y ** 0.25

Z2 = X ** 2 - Y ** 2

Z3 = 2 * X + 3 * Y

Z4 = 2 + 2 * X + +2 * Y - X ** 2 - Y ** 2

# Построение графиков

fig = plt.figure(figsize=(15, 8))

ax1 = fig.add_subplot(221, projection='3d')
ax1.plot_surface(X, Y, Z1, cmap='viridis')
ax1.set_title('z=x^0.25+y^0.25')

ax2 = fig.add_subplot(222, projection='3d')
ax2.plot_surface(X, Y, Z2, cmap='viridis')
ax2.set_title('z= x^2 -y^2')

ax2 = fig.add_subplot(223, projection='3d')
ax2.plot_surface(X, Y, Z2, cmap='viridis')
ax2.set_title('z= 2+2x+2y-x^2-y^2')


plt.tight_layout()
plt.show()
import numpy as np


def ctg(x):
    return 1 / np.tan(x)


a = float(0.3)
b = float(-21.17)
z = ctg(np.pi / 4 - 1) + np.power(a + 1.5, 1 / 3) - b / np.power(np.arcsin(np.abs(a)), 2)
print("Ответ: " + str(z))

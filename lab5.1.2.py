import numpy as np

N = 30
X = np.column_stack((np.ones(12), np.arange(N, N + 12), np.random.randint(60, 83, size=12)))

Y = np.array([13.5,13.9,14.3,14.6,14.9,15.8,16.1,16.7,17.2,17.7,18.3,18.6])

X_transpose = X.T

XTX = np.dot(X_transpose, X)
XTX_inverse = np.linalg.inv(XTX)
XTY = np.dot(X_transpose, Y)

A = np.dot(XTX_inverse, XTY)

Y_pred = A[0] + A[1] * X[:, 1] + A[2] * X[:, 2]
MSE = np.mean((Y - Y_pred) ** 2)

print("Оценка А: ", A)
print("Исходные данные Y:", Y)
print("Значения Y(предсказанные):", Y_pred)
print("Среднеквадратичная ошибка(MSE)", MSE)

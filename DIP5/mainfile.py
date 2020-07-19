import cv2
import matplotlib.pylab as plt
import PIL
import numpy as np

original_image = np.ones((17, 17))

S_K = []
for i in range(16):
    S_K.append(complex(i, 0))
for i in range(16):
    S_K.append(complex(16, i))
for i in range(16):
    S_K.append(complex(16 - i, 16))
for i in range(16):
    S_K.append(complex(0 ,16 - i))

for i in range(17):

    for j in range(17):
        if i == 0 or i == 16 or j == 0 or j == 16:
            original_image[i][j] = 0


plt.imshow(original_image, cmap="gray")
plt.show()
K = len(S_K)
A_U = []
for u in range(K):
    a_u = 0
    for k in range(K):
        a_u += S_K[k] * np.exp(-1 * complex(0, 1) * 2 * np.pi * u * k / K)
    A_U.append(a_u / K)

P = 32
S_K_HAT = []
for k in range(K):
    s_k_hat = 0
    for u in range(P):
        s_k_hat += A_U[u] * np.exp(complex(0, 1) * 2 * np.pi * u * k / K)

    S_K_HAT.append(s_k_hat)
new_matrix = np.ones((17, 17))
a = len(S_K_HAT)
for index, item in enumerate(S_K_HAT):

    x = int(item.real)
    y = int(item.imag)
    if x < 17 and y < 17:
        new_matrix[int(x)][int(y)] = 0

plt.imshow(new_matrix, cmap="gray")
plt.show()

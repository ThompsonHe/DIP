from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

'''
FFT,快速傅里叶变换
'''


def my_fft(img_array):
    height = img_array.shape[0]
    width = img_array.shape[1]

    result_complex = img_array.astype(np.complex)

    def fft_one(a):
        len = a.size
        if len == 1:
            return

        a0 = np.zeros(len // 2, complex)
        a1 = np.zeros(len // 2, complex)
        for i in range(0, len, 2):
            a0[i // 2] = a[i]
            a1[i // 2] = a[i + 1]
        fft_one(a0)
        fft_one(a1)

        wn = complex(np.cos(2 * np.pi / len), np.sin(2 * np.pi / len))  # 参数
        w = complex(1, 0)
        for i in range(len // 2):
            t = w * a1[i]
            a[i] = a0[i] + t
            a[i + len // 2] = a0[i] - t
            w = w * wn

    for i in range(height):
        fft_one(result_complex[i])
    for i in range(width):
        fft_one(result_complex[:, i])

    return result_complex


'''
IFFT,快速傅里叶逆变换
'''


def my_ifft(img_array):
    height = img_array.shape[0]
    width = img_array.shape[1]

    result_complex = img_array.astype(np.complex)
    result = np.zeros([height, width], np.float64)

    def ifft_one(a):
        len = a.size
        if len == 1:
            return

        a0 = np.zeros(len // 2, complex)
        a1 = np.zeros(len // 2, complex)
        for i in range(0, len, 2):
            a0[i // 2] = a[i]
            a1[i // 2] = a[i + 1]
        ifft_one(a0)
        ifft_one(a1)

        wn = complex(np.cos(2 * np.pi / len), -1 * np.sin(2 * np.pi / len))  # 参数
        w = complex(1, 0)
        for i in range(len // 2):
            t = w * a1[i]
            a[i] = a0[i] + t
            a[i + len // 2] = a0[i] - t
            w = w * wn

    for i in range(height):
        ifft_one(result_complex[i])
    for i in range(width):
        ifft_one(result_complex[:, i])

    for i in range(height):
        for j in range(width):
            result[i, j] = np.abs(result_complex[i, j] / (height * width))

    # 返回结果
    return result


image = np.zeros((64, 64))
median = [31, 32]
for i in median:
    for j in median:
        image[i][j] = 1

myfft = my_fft(image)
myfft_abs = np.abs(myfft)
center = np.fft.fftshift(myfft_abs)  # 把结果移到中间
myifft = my_ifft(myfft)

plt.subplot(1, 3, 1)
plt.title("original image")
plt.imshow(image, cmap="gray")

plt.subplot(1, 3, 2)
plt.title("FFT")
plt.imshow(center, cmap="gray")

plt.subplot(1, 3, 3)
plt.title("IFFT")
plt.imshow(myifft, cmap="gray")

plt.show()
"""

边缘检测
编程实现基于典型微分算子（不少于Roberts、Sobel、Prewitt、拉普拉斯算子）的图像边缘提取，能够读取图像文件内容，进行检测后输出边缘检测结果
分析比较不同算子的特性
感兴趣的同学可尝试实现其他边缘检测算子

"""
import numpy as np
import cv2
import matplotlib.pylab as plt

def convolution_2d(image, filter):

    new_image = np.zeros((image.shape[0], image.shape[1]))
    filter = filter.flatten()
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):

            if i == 0 or i == image.shape[0] - 1 or j == 0 or j == image.shape[1] - 1:
                new_image[i][j] = image[i][j]
            else:
                value = 0
                filter_index = 0
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        value += image[i + x][j + y] * filter[filter_index]
                        filter_index += 1
                if value < 0:
                    new_image[i][j] = 0
                elif value > 255:
                    new_image[i][j] = 255
                else:
                    new_image[i][j] = value

    return  new_image



def Roberts_Operater(image):
    new_image_1 = np.zeros((image.shape[0], image.shape[1]))
    new_image_2 = np.zeros((image.shape[0], image.shape[1]))
    new_image = np.zeros((image.shape[0], image.shape[1]))
    filter_1 = np.array([[-1, 0],
                      [0, 1]]).flatten()
    filter_2 = np.array([[0, -1],
                         [1, 0]]).flatten()
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if i == image.shape[0] - 1 or j == image.shape[1] - 1:
                new_image_1[i][j] = 0
                new_image_2[i][j] = 0
                new_image[i][j] = 0
            else:
                value_1 = 0
                value_2 = 0
                filter_index = 0

                for x in range(0, 2):
                    for y in range(0, 2):
                        value_1 += image[i + x][j + y] * filter_1[filter_index]
                        value_2 += image[i + x][j + y] * filter_2[filter_index]
                        filter_index += 1
                new_image_1[i][j] = value_1
                new_image_2[i][j] = value_2
                temp = value_1 + value_2
                if temp < 0:
                    temp = 0
                elif temp > 255:
                    temp = 255
                new_image[i][j] = temp


    plt.subplot(2, 2, 1)
    plt.title("pre-image")
    plt.axis("off")
    plt.imshow(image, cmap="gray")

    plt.subplot(2, 2, 2)
    plt.title("post-image")
    plt.axis("off")
    plt.imshow(new_image, cmap="gray")

    plt.subplot(2, 2, 3)
    plt.title("feature-map-1")
    plt.axis("off")
    plt.imshow(new_image_1, cmap="gray")

    plt.subplot(2, 2, 4)
    plt.title("feature-map-2")
    plt.axis("off")
    plt.imshow(new_image_2, cmap="gray")

    plt.show()
    return new_image




def Sobel_Operater(image):
    """
    -1  -2  -1        -1  0  1
     0   0   0         -2  0  2
     1   2   1         -1  0  1
    """
    vertical_feature_extraction_filter = np.array([[-1, -2, -1],
                                                   [0, 0, 0],
                                                   [1, 2, 1]])
    horizontal_feature_extraction_filter = np.array([[-1, 0, 1],
                                                     [-2, 0, 2],
                                                     [-1, 0, 1]])
    new_image = np.zeros((image.shape[0], image.shape[1]))
    new_image_vertical = convolution_2d(image, horizontal_feature_extraction_filter)
    new_image_horizontal = convolution_2d(image, vertical_feature_extraction_filter)

    #image tune
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            value = new_image_horizontal[i][j] + new_image_vertical[i][j]

            if value < 0:
                new_image[i][j] = 0
            elif value > 255:
                new_image[i][j] = 255
            else:
                new_image[i][j] = value
    plt.subplot(2, 2, 1)
    plt.title("original-image")
    plt.axis("off")
    plt.imshow(image, cmap="gray")

    plt.subplot(2, 2, 2)
    plt.title("processed-image")
    plt.axis("off")
    plt.imshow(new_image, cmap="gray")

    plt.subplot(2, 2, 3)
    plt.title("x-orientation")
    plt.axis("off")
    plt.imshow(new_image_horizontal, cmap="gray")

    plt.subplot(2, 2, 4)
    plt.title("y-orientation")
    plt.axis("off")
    plt.imshow(new_image_vertical, cmap="gray")

    plt.show()
    return new_image



def Prewitt_Operater(image):
    """
    -1  -1  -1         -1  0  1
     0   0   0         -1  0  1
     1   1   1         -1  0  1
    """
    vertical_feature_extraction_filter = np.array([[-1, -1, -1],
                                                   [0, 0, 0],
                                                   [1, 1, 1]])
    horizontal_feature_extraction_filter = np.array([[-1, 0, 1],
                                                     [-1, 0, 1],
                                                     [-1, 0, 1]])

    new_image = np.zeros((image.shape[0], image.shape[1]))
    new_image_vertical = convolution_2d(image, horizontal_feature_extraction_filter)
    new_image_horizontal = convolution_2d(image, vertical_feature_extraction_filter)


    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            value = new_image_horizontal[i][j] + new_image_vertical[i][j]

            if value < 0:
                new_image[i][j] = 0
            elif value > 255:
                new_image[i][j] = 255
            else:
                new_image[i][j] = value

    plt.subplot(2, 2, 1)
    plt.title("original-image")
    plt.axis("off")
    plt.imshow(image, cmap="gray")

    plt.subplot(2, 2, 2)
    plt.title("processed-image")
    plt.axis("off")
    plt.imshow(new_image, cmap="gray")

    plt.subplot(2, 2, 3)
    plt.title("x-orientation")
    plt.axis("off")
    plt.imshow(new_image_horizontal, cmap="gray")

    plt.subplot(2, 2, 4)
    plt.title("y-orientation")
    plt.axis("off")
    plt.imshow(new_image_vertical, cmap="gray")

    plt.show()
    return new_image




def Laplace_Operater(image):
    filter = np.array([[0, -1, 0],
                       [-1, 4, -1],
                       [0, -1, 0]])
    new_image = convolution_2d(image, filter)

    plt.subplot(1, 2, 1)
    plt.title("pre-image")
    plt.axis("off")
    plt.imshow(image, cmap="gray")

    plt.subplot(1, 2, 2)
    plt.title("post-image")
    plt.axis("off")
    plt.imshow(new_image, cmap="gray")

    plt.show()
    return new_image




def main():
    image = cv2.imread("1.png")
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    prewitt = Prewitt_Operater(gray)
    sobel = Sobel_Operater(gray)
    laplace = Laplace_Operater(gray)
    roberts = Roberts_Operater(gray)

    plt.subplot(2, 2, 1)
    plt.title("prewitt-operater")
    plt.axis("off")
    plt.imshow(prewitt, cmap="gray")

    plt.subplot(2, 2, 2)
    plt.title("sobel-operater")
    plt.axis("off")
    plt.imshow(sobel, cmap="gray")

    plt.subplot(2, 2, 3)
    plt.title("laplace-operater")
    plt.axis("off")
    plt.imshow(laplace, cmap="gray")

    plt.subplot(2, 2, 4)
    plt.title("roberts-operater")
    plt.axis("off")
    plt.imshow(roberts, cmap="gray")

    plt.show()


if __name__ == '__main__':
    main()
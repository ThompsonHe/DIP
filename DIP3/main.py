# coding=gbk
import matplotlib.pylab as plt
import cv2
import numpy as np


# ֱ��ͼ���⻯����
def histogram_mean_processing(img):
    total_pixels_number = img.shape[0] * img.shape[1]  # ��ͼ����������
    height, width = img.shape[0], img.shape[1]
    mini_value = img[0][0]
    max_value = img[0][0]
    value_list = np.zeros((256), dtype="int")
    for i in range(height):
        for j in range(width):
            value = img[i][j]
            value_list[value] += 1
            if value < mini_value:
                mini_value = value
            elif value > max_value:
                max_value = value
    accumulation = 0
    distribution_list = []
    print("���ֵ�Ҷ�ֵΪ{}, ��С�Ҷ�ֵΪ{}".format(str(max_value), str(mini_value)))
    for i, number in enumerate(value_list):  # i�ǻҶ�ֵ number�ǸûҶ�ֵ�����ص�ĸ���

        accumulation += number

        ratio = float(accumulation / total_pixels_number)

        distribution_list.append(ratio)
    print(distribution_list)

    new_image = np.zeros((height, width), dtype="int")
    for i in range(height):
        for j in range(width):
            pre_value = img[i][j]
            post_value = int(distribution_list[pre_value] * 255)
            new_image[i][j] = post_value
    return new_image


def median_filtering(image, scale=7):

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            #����Ǵ��ڱ߽磬��ֱ�Ӹ�ֵ
            if i < int(scale/2) or i >= image.shape[0] - int(scale/2) or j < int(scale/2) or j >= image.shape[1] - int(scale/2):
                continue
                #print("({},{})".format(str(i), str(j)))
            else:
                region_list = []
                #����һ���Ե�ǰ���ص�Ϊ���ĵ�3x3������
                for x in range(i - int(scale/2), i + int(scale/2) + 1):
                    for y in range(j - int(scale/2), j + int(scale/2) + 1):
                        region_list.append(image[x][y])
                region_list.sort()
                image[i][j] = region_list[int(pow(scale, 2)/2)]
    return image


def image_enhancement_via_exponential_transformation(image, param):
    new_image = np.zeros((image.shape[0], image.shape[1]))
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            new_image[i][j] = np.power(image[i][j], param)
    return new_image



def laplacian_sharpening(image):
    """

    0 -1 0
    -1 4 -1
    0 1  0

    """
    new_image = np.zeros((image.shape[0], image.shape[1]))
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if i == 0 or i == image.shape[0] - 1 or j == 0 or j == image.shape[1] - 1:
                new_image[i][j] = image[i][j]
            else:
                new_image[i][j] = image[i - 1][j] * -1 + image[i][j] * 4 + image[i][j - 1] * -1 + image[i][j + 1] * -1 + image[i + 1][j] * -1
    print("hello")
    return new_image



def histogram_mean_processing_view(image):
    channel_1, channel_2, channel_3 = image[:, :, 0], image[:, :, 1], image[:, :, 2]
    pre_image = cv2.merge([channel_3, channel_2, channel_1])
    processed_channel_1 = histogram_mean_processing(channel_1)
    processed_channel_2 = histogram_mean_processing(channel_2)
    processed_channel_3 = histogram_mean_processing(channel_3)
    processed_image = cv2.merge([processed_channel_3, processed_channel_2, processed_channel_1])
    print("- - - - - - - - - ���ڻ���ͼƬ�����Ժ�- - - - - - - - - -")

    # ����ԭͼƬ
    plt.subplot(1, 2, 1)
    plt.title('pre-processed image')
    plt.axis("off")
    plt.imshow(pre_image)
    # ���ƴ�����ͼƬ
    plt.subplot(1, 2, 2)
    plt.title('post-processed image')
    plt.axis("off")
    plt.imshow(processed_image)
    plt.show()

    print("- - - - - - - - -���ڻ���ֱ��ͼ���Ժ�- - - - - - - - - -")
    # ����ͼƬ����ǰ����ͨ����ֱ��ͼ
    plt.subplot(2, 3, 1)
    plt.title("pre-channel_1")
    plt.hist(channel_1, facecolor="red")

    plt.subplot(2, 3, 2)
    plt.title("pre-channel_2")
    plt.hist(channel_2, facecolor="green")

    plt.subplot(2, 3, 3)
    plt.title("pre-channel_3")
    plt.hist(channel_3, facecolor="blue")

    # ����ͼƬ��������ͨ����ֱ��ͼ
    plt.subplot(2, 3, 4)
    plt.title("processed-channel_1")
    plt.hist(processed_channel_1, facecolor="red")

    plt.subplot(2, 3, 5)
    plt.title("processed-channel_2")
    plt.hist(processed_channel_2, facecolor="green")

    plt.subplot(2, 3, 6)
    plt.title("processed-channel_3")
    plt.hist(processed_channel_3, facecolor="blue")

    plt.show()

def median_filtering_view(image, scale=3):

    if scale % 2 == 0:
        raise ValueError("����Ӧ��Ϊ����")
    elif scale < 3:
        raise ValueError("���������3������")

    channel_1, channel_2, channel_3 = image[:, :, 0], image[:, :, 1], image[:, :, 2]
    pre_image = cv2.merge([channel_3, channel_2, channel_1])
    processed_channel_1 = median_filtering(channel_1, scale)
    processed_channel_2 = median_filtering(channel_2, scale)
    processed_channel_3 = median_filtering(channel_3, scale)
    post_image = cv2.merge([processed_channel_3, processed_channel_2, processed_channel_1])

    plt.subplot(1, 2, 1)
    plt.title('pre-image')
    plt.imshow(pre_image)

    plt.subplot(1, 2, 2)
    plt.title('post-image')
    plt.imshow(post_image)

    plt.show()

def laplacian_sharpening_view(image):

    boundary_image = laplacian_sharpening(image)
    new_image = np.zeros((image.shape[0], image.shape[1]))

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):

           value = boundary_image[i][j] + image[i][j]
           if  value > 255:
               value = 255
           elif value < 0:
               value = 0
           new_image[i][j] = value

    plt.subplot(1, 2, 1)
    plt.title("pre-image")
    plt.imshow(image, cmap="gray")

    plt.subplot(1, 2, 2)
    plt.title("post-image")
    plt.imshow(new_image, cmap="gray")

    plt.show()


def image_enhancement_via_exponential_transformation_view(image, param):

    new_image = image_enhancement_via_exponential_transformation(image, param)

    plt.subplot(1, 2, 1)
    plt.title("pre-image")
    plt.imshow(image, cmap="gray")

    plt.subplot(1, 2, 2)
    plt.title("post-image:e = {}".format(str(param)))
    plt.imshow(new_image, cmap="gray")

    plt.show()




def main():
    image1 = cv2.imread("3.png")
    image2 = cv2.imread("noIse.png")
    gray = cv2.cvtColor(image1, cv2.COLOR_RGB2GRAY)
    histogram_mean_processing_view(image1)
    median_filtering_view(image2, 3) #3x3 5x5 7x7���˲��ߴ�
    laplacian_sharpening_view(gray)
    image_enhancement_via_exponential_transformation_view(gray, 1.6)




if __name__ == "__main__":
    main()

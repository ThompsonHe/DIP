import cv2
import numpy as np
import matplotlib.pylab as plt
import sys
import math


def byte_to_int(num):
    return int.from_bytes(num, byteorder="little")

def int_to_byte(num):
    pass
def is_in_array(x, y, height, width):
    if (x >= 0 and x < width and y >= 0 and y < height):

        return 1
    else:
        return 0
def bilininterpolation(channel, times):
    height_out = int(channel.shape[0] * times)

    width_out = int(channel.shape[1] * times)

    new_data = np.zeros((height_out, width_out))

    for row in range(height_out):

        for col in range(width_out):

            x = int(row / times)

            y = int(col / times)

            x1 = x + 1

            x2 = x - 1

            y1 = y + 1

            y2 = y - 1

            f11, f12, f21, f22 = 0, 0, 0, 0
            if is_in_array(x1, y1, channel.shape[0], channel.shape[1]):
                f11 = channel[x1][y1]

            if is_in_array(x1, y2, channel.shape[0], channel.shape[1]):
                f12 = channel[x1][y2]

            if is_in_array(x2, y1, channel.shape[0], channel.shape[1]):
                f21 = channel[x2][y1]

            if is_in_array(x2, y2, channel.shape[0], channel.shape[1]):
                f22 = channel[x2][y2]

            new_data[row][col] = ((f11 * (x2 - x) * (y2 - y) +
                                   f21 * (x - x1) * (y2 - y) +
                                   f12 * (x2 - x) * (y - y1) +
                                   f22 * (x - x1) * (y - y1))) / ((x2 - x1) * (y2 - y1))

    return new_data


class BMP:

    def __init__(self, file_name):

        file = open(file_name, "rb")

        """读取bmp文件的文件头14字节"""
        self.byType = file.read(2)  # 0x4d42 对应BM 表示这是Windows支持的位图格式
        self.bfSize = byte_to_int(file.read(4))  # 位图文件大小
        self.bfReserved1 = byte_to_int(file.read(2))  # 保留字段 必须设为 0
        self.bfReserved2 = byte_to_int(file.read(2))  # 保留字段 必须设为 0
        self.bfOffBits = byte_to_int(file.read(4))  # 偏移量 从文件头到位图数据需偏移多少字节（位图信息头、调色板长度等不是固定的，这时就需要这个参数了

        """读取bmp文件的位图信息头40字节"""
        self.biSize = byte_to_int(file.read(4))  # 所需要的字节数
        self.biWidth = byte_to_int(file.read(4))  # 图像的宽度 单位 像素
        self.biHeight = byte_to_int(file.read(4))  # 图像的高度 单位 像素
        self.biPlanes = byte_to_int(file.read(2))  # 说明颜色平面数 为常量1
        self.biBitCount = byte_to_int(file.read(2))  # 说明比特数

        self.biCompression = byte_to_int(file.read(4))  # 图像的高度 单位 像素
        self.biSizeImage = byte_to_int(file.read(4))  # 图像大小
        self.biXPelsPerMeter = byte_to_int(file.read(4))  # 水平分辨率
        self.biYPelsPerMeter = byte_to_int(file.read(4))  # 垂直分辨率
        self.biClrUsed = byte_to_int(file.read(4))  # 实际使用的彩色表中的颜色索引数
        self.biClrImportant = byte_to_int(file.read(4))  # 对图像显示有重要影响的颜色索引的数目
        self.bmp_data = []


        # 如果文件过大，报错

        if self.biWidth >= 1000:
            self.raise_error("文件尺寸过大")
            sys.exit(0)

        if self.biBitCount == 24:  # 彩色图片

            begin = 54

            while (begin != self.bfOffBits):
                begin = begin + 1
                file.read(1)
            r = []
            g = []
            b = []

            for height in range(self.biHeight):

                r_channel = []
                g_channel = []
                b_channel = []

                for width in range(self.biWidth):
                    R_temp = byte_to_int(file.read(1))
                    G_temp = byte_to_int(file.read(1))
                    B_temp = byte_to_int(file.read(1))
                    #bmp_data_row.append([B_temp, G_temp, R_temp])
                    r_channel.append(R_temp)
                    g_channel.append(G_temp)
                    b_channel.append(B_temp)
                r.append(r_channel)
                g.append(g_channel)
                b.append(b_channel)
            r.reverse()
            g.reverse()
            b.reverse()

            self.rgb = [r, g, b]
            r_channel = np.array(r).reshape((self.biHeight, self.biWidth))
            g_channel = np.array(g).reshape((self.biHeight, self.biWidth))
            b_channel = np.array(b).reshape((self.biHeight, self.biWidth))
            a = np.stack((b_channel, g_channel, r_channel), axis=2)
            self.bmp_data = np.stack((b_channel, g_channel, r_channel), axis=2)
            #print(self.bmp_data.shape)
            #plt.imshow(self.bmp_data)
            #print(self.bmp_data)
            #plt.show()
            file.close()


        elif self.biBitCount == 8:
            begin = 54
            while (begin != self.bfOffBits):
                begin = begin + 1
                file.read(1)
            for height in range(self.biWidth):
                row_pix = []
                for row in range(self.biHeight):
                    row_pix.append(byte_to_int(file.read(1)))
                # row_pix.reverse()
                self.bmp_data.append(row_pix)

            self.bmp_data.reverse()
            self.bmp_data = np.array(self.bmp_data).reshape(self.biWidth, self.biHeight)
            # print(self.bmp_data)
            plt.imshow(self.bmp_data, cmap="gray")
            plt.show()

    """图片的尺度"""

    @property
    def image_shape(self):
        return np.array([self.biHeight, self.biWidth])

    """图片的色深"""

    @property
    def bit_count(self):
        return self.biBitCount

    """图片加操作"""

    def image_add(self, object):

        if self.image_shape[0] != object.image_shape[0] and self.image_shape[1] != self.image_shape[1]:
            self.raise_error("两张图片的尺寸不同")
            sys.exit(0)

        # 如果两张图片的比特数不相同
        if self.biBitCount != object.biBitCount:
            self.raise_error("两张图片的比特数不同")
            sys.exit(0)

        # 如果是8bit bmp文件
        if self.biBitCount == 8:

            return 0.5 * self.bmp_data + 0.5 * object.bmp_data

        # 如果是24bit bmp文件
        elif self.biBitCount == 24:
            res = []
            for row in range(self.biHeight):

                for col in range(self.biWidth):
                    temp = 0.5 * self.bmp_data[row][col] + 0.5 * object.bmp_data[row][col]

                    res.append(temp)
            res = np.array(res).reshape(self.biHeight, self.biWidth, 3)
            return res / 255
        else:

            self.raise_error("既不是8bit文件也不是24bit文件")

    """
    图像的几何变换：
    
    平移、
    
    旋转、
    
    水平镜像、
    
    垂直镜像、
    
    放缩变换、
    
    """

    """报错"""
    def raise_error(self, str):
        print(str)

    """图片旋转"""

    def rotation(self, angle):

        # 24位色彩bmp文件
        if self.biBitCount == 24:  #rotation 的还没写

            channel_r = np.zeros((self.biHeight, self.biWidth))
            channel_g = np.zeros((self.biHeight, self.biWidth))
            channel_b = np.zeros((self.biHeight, self.biWidth))
            angle = 1 * angle * np.pi / 180
            midX_pre = self.biWidth // 2
            midY_pre = self.biHeight // 2
            midX_aft = self.biWidth // 2
            midY_aft = self.biHeight // 2
            a = self.bmp_data
            for i in range(self.biHeight):
                for j in range(self.biWidth):

                    after_i = i - midY_aft
                    after_j = j - midX_aft

                    pre_i = (int)(np.cos(angle) * after_i - np.sin(angle) * after_j) + midY_pre
                    pre_j = (int)(np.sin(angle) * after_i + np.cos(angle) * after_j) + midX_pre

                    if pre_i >=0 and pre_i < self.biHeight and pre_j >= 0 and pre_j < self.biWidth:
                        channel_r[i, j] = self.bmp_data[pre_i][pre_j][0]
                        channel_g[i, j] = self.bmp_data[pre_i][pre_j][1]
                        channel_b[i, j] = self.bmp_data[pre_i][pre_j][2]

            image = cv2.merge([channel_r,channel_g,channel_b]).astype(np.int64)
            self.generate(image)
            #plt.imshow(image)
            #plt.show()








        # 8位色彩bmp文件
        else:

            new_image = np.zeros((self.biHeight, self.biWidth))
            angle = 1 * angle * np.pi / 180
            midX_pre = self.biWidth // 2
            midY_pre = self.biHeight // 2
            midX_aft = self.biWidth
            midY_aft = self.biHeight
            a = self.bmp_data
            for i in range(self.biHeight):
                for j in range(self.biWidth):

                    after_i = i - midY_aft
                    after_j = j - midX_aft

                    pre_i = (int)(np.cos(angle) * after_i - np.sin(angle) * after_j) + midY_pre
                    pre_j = (int)(np.sin(angle) * after_i + np.cos(angle) * after_j) + midX_pre

                    if pre_i >= 0 and pre_i < self.biHeight and pre_j >= 0 and pre_j < self.biWidth:
                        new_image[i, j] = self.bmp_data[pre_i][pre_j]
            new_image = new_image.astype(np.int64)
            #plt.imshow(new_image, cmap="gray")
            #plt.show()
            self.generate(new_image)
    """图像平移"""
    def shift(self, X, Y):

        if self.biBitCount == 8:

            new_mat = np.zeros((self.biHeight, self.biWidth))

            for row in range(self.biHeight):

                for col in range(self.biWidth):

                    value = self.bmp_data[row][col]

                    x = row + X
                    y = col + Y

                    if int(x) >= 0 and int(x) < self.biWidth and int(y) >= 0 and int(y) < self.biHeight:
                        new_mat[int(x)][int(y)] = int(value)
            self.generate(new_mat)
            #plt.imshow(new_mat, cmap="gray")
            #plt.show()

        elif self.biBitCount == 24:

            new_mat = np.zeros([self.biHeight, self.biWidth, 3])

            for row in range(self.biHeight):

                for col in range(self.biWidth):

                    value = self.bmp_data[row][col]
                    x = row + X
                    y = col + Y

                    if int(x) >= 0 and int(x) < self.biWidth and int(y) >= 0 and int(y) < self.biHeight:
                        new_mat[int(x), int(y), :] = value
            self.generate(new_mat)
            #plt.imshow(new_mat / 255)
            #plt.show()


    """图像水平镜像"""
    def mirror_horizontal(self):

        if self.biBitCount == 8:

            new_mat = np.zeros((self.biHeight, self.biWidth))

            for row in range(self.biHeight):

                for col in range(self.biWidth):

                    value = self.bmp_data[row][col]

                    x = row

                    y = self.biHeight - col

                    if int(x) >= 0 and int(x) < self.biWidth and int(y) >= 0 and int(y) < self.biHeight:
                        new_mat[int(x)][int(y)] = value
            self.generate(new_mat)
            #plt.imshow(new_mat, cmap="gray")
            #plt.show()

        elif self.biBitCount == 24:

            new_mat = np.zeros([self.biHeight, self.biWidth, 3])

            for row in range(self.biHeight):

                for col in range(self.biWidth):

                    value = self.bmp_data[row][col]
                    # print(value)

                    x = row
                    y = self.biHeight - col

                    if int(x) >= 0 and int(x) < self.biWidth and int(y) >= 0 and int(y) < self.biHeight:
                        new_mat[int(x), int(y), :] = value
            self.generate(new_mat)

            #plt.imshow(new_mat / 255)
            #plt.show()

    """图像垂直镜像"""
    def mirror_vertical(self):

        if self.biBitCount == 8:

            new_mat = np.zeros((self.biHeight, self.biWidth))

            for row in range(self.biHeight):

                for col in range(self.biWidth):

                    value = self.bmp_data[row][col]

                    x = self.biHeight - row

                    y = col

                    if int(x) >= 0 and int(x) < self.biWidth and int(y) >= 0 and int(y) < self.biHeight:
                        new_mat[int(x)][int(y)] = value

            #plt.imshow(new_mat, cmap="gray")
            #plt.show()
            self.generate(new_mat)

        elif self.biBitCount == 24:

            new_mat = np.zeros([self.biHeight, self.biWidth, 3])

            for row in range(self.biHeight):

                for col in range(self.biWidth):

                    value = self.bmp_data[row][col]
                    # print(value)

                    x = self.biHeight - row
                    y = col

                    if int(x) >= 0 and int(x) < self.biWidth and int(y) >= 0 and int(y) < self.biHeight:
                        new_mat[int(x), int(y), :] = value

            #plt.imshow(new_mat / 255)
            #plt.show()
            self.generate(new_mat)

    """双线性插值缩放"""

    def resize_image(self, times):

        if self.biBitCount == 8:

            result = bilininterpolation(self.bmp_data, times)
            #plt.imshow(result, cmap="gray")
            #plt.show()
            self.generate(result)
        elif self.biBitCount == 24:

            R_channel = self.bmp_data[:, :, 0]

            G_channel = self.bmp_data[:, :, 1]

            B_channel = self.bmp_data[:, :, 2]


            channel_out_R = bilininterpolation(R_channel, times)

            channel_out_G = bilininterpolation(G_channel, times)

            channel_out_B = bilininterpolation(B_channel, times)

            new_data = np.zeros((int(self.biHeight * times), int(self.biWidth * times), 3))

            new_data[:, :, 0] = channel_out_R
            new_data[:, :, 1] = channel_out_G
            new_data[:, :, 2] = channel_out_B

            #plt.imshow(new_data)
            #plt.show()
            self.generate(new_data)

    """图像求反操作"""
    def invert(self):

        result = 255 - self.bmp_data

        #plt.imshow(result / 255)
        #plt.show()
        self.generate(result)

    """变更bmpdata"""
    def generate(self, data):
        self.bmp_data = data
        #print(self)
        #return self












# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MyForm.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import os
from tkinter import Image

import matplotlib
import numpy as np
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QFileDialog, QGraphicsPixmapItem, QGraphicsScene, QVBoxLayout, QLabel
import matplotlib.pylab as plt


matplotlib.use("Qt5Agg")  # 声明使用QT5

from matplotlib.figure import Figure

from bmp import BMP


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1492, 1200)
        Form.setWindowTitle("图像处理框架DEMO")

        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 751, 621))
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setTitle("图像1")

        self.pushButton1 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton1.setGeometry(QtCore.QRect(590, 80, 113, 32))
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton1.setText("选择图像")
        self.pushButton1.clicked.connect(self.select_image_1)

        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit.setGeometry(QtCore.QRect(40, 80, 521, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setEnabled(False)

        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(610, 211, 79, 71))
        self.label.setObjectName("label")
        self.label.setText("图像水平位移")

        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(610, 380, 78, 18))
        self.label_2.setObjectName("label_2")
        self.label_2.setText("图像水平镜像")

        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(610, 280, 79, 72))
        self.label_3.setObjectName("label_3")
        self.label_3.setText("图  像    旋  转")

        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(610, 449, 78, 18))
        self.label_4.setObjectName("label_4")
        self.label_4.setText("图像垂直镜像")

        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(610, 490, 79, 71))
        self.label_5.setObjectName("label_5")
        self.label_5.setText("图  像    缩  放")

        self.txtShiftHor1 = QtWidgets.QTextEdit(self.groupBox)
        self.txtShiftHor1.setGeometry(QtCore.QRect(610, 260, 81, 31))
        self.txtShiftHor1.setObjectName("txtShiftHor1")
        self.txtShiftHor1.setText("0")

        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(610, 170, 81, 16))
        self.label_6.setObjectName("label_6")
        self.label_6.setText("图像竖直位移")

        self.txtRotation1 = QtWidgets.QTextEdit(self.groupBox)
        self.txtRotation1.setGeometry(QtCore.QRect(610, 330, 81, 31))
        self.txtRotation1.setObjectName("txtRotation1")
        self.txtRotation1.setText("0")

        self.txtScale1 = QtWidgets.QTextEdit(self.groupBox)
        self.txtScale1.setGeometry(QtCore.QRect(610, 540, 81, 31))
        self.txtScale1.setObjectName("txtScale1")
        self.txtScale1.setText("0")

        self.txtShitfVer1 = QtWidgets.QTextEdit(self.groupBox)
        self.txtShitfVer1.setGeometry(QtCore.QRect(610, 190, 81, 31))
        self.txtShitfVer1.setObjectName("txtShitfVer1")
        self.txtShitfVer1.setText("0")

        self.pushBtnExec1 = QtWidgets.QPushButton(self.groupBox)
        self.pushBtnExec1.setGeometry(QtCore.QRect(590, 580, 113, 32))
        self.pushBtnExec1.setObjectName("pushBtnExec1")
        self.pushBtnExec1.setText("执行操作")
        self.pushBtnExec1.clicked.connect(self.execution_0)

        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(610, 480, 87, 22))
        self.layoutWidget.setObjectName("layoutWidget")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.radioBtn1_2_1 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioBtn1_2_1.setObjectName("radioBtn1_2_1")
        self.radioBtn1_2_1.setText("是")
        self.horizontalLayout_2.addWidget(self.radioBtn1_2_1)

        self.radioBtn1_2_0 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioBtn1_2_0.setObjectName("radioBtn1_2_0")
        self.radioBtn1_2_0.setText("否")
        self.radioBtn1_2_0.setChecked(True)
        self.horizontalLayout_2.addWidget(self.radioBtn1_2_0)

        self.pushBtnExec1_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushBtnExec1_3.setGeometry(QtCore.QRect(30, 580, 113, 32))
        self.pushBtnExec1_3.setObjectName("pushBtnExec1_3")
        self.pushBtnExec1_3.setText("图像取反")
        self.pushBtnExec1_3.clicked.connect(self.invert_0)

        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(610, 410, 87, 22))
        self.widget.setObjectName("widget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.radioBtn1_1_1 = QtWidgets.QRadioButton(self.widget)
        self.radioBtn1_1_1.setObjectName("radioBtn1_1_1")
        self.radioBtn1_1_1.setText("是")
        self.horizontalLayout.addWidget(self.radioBtn1_1_1)
        self.radioBtn1_1_0 = QtWidgets.QRadioButton(self.widget)
        self.radioBtn1_1_0.setObjectName("radioBtn1_1_0")
        self.radioBtn1_1_0.setText("否")
        self.radioBtn1_1_0.setChecked(True)
        self.horizontalLayout.addWidget(self.radioBtn1_1_0)

        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(750, 0, 751, 621))
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_2.setTitle("图像2")

        self.pushButton1_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton1_2.setGeometry(QtCore.QRect(580, 80, 113, 32))
        self.pushButton1_2.setObjectName("pushButton1_2")
        self.pushButton1_2.setText("选择图像")
        self.pushButton1_2.clicked.connect(self.select_image_2)

        self.textEdit_2 = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit_2.setGeometry(QtCore.QRect(30, 80, 521, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setEnabled(False)

        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(610, 449, 78, 18))
        self.label_7.setObjectName("label_7")
        self.label_7.setText("图像垂直镜像")

        self.pushBtnExec2 = QtWidgets.QLabel(self.groupBox_2)
        self.pushBtnExec2.setGeometry(QtCore.QRect(610, 490, 79, 71))
        self.pushBtnExec2.setObjectName("pushBtnExec2")
        self.pushBtnExec2.setText("图 像     缩 放")

        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(610, 211, 79, 71))
        self.label_9.setObjectName("label_9")
        self.label_9.setText("图像水平位移")

        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(610, 380, 78, 18))
        self.label_10.setObjectName("label_10")
        self.label_10.setText("图像水平镜像")

        self.txtScale2 = QtWidgets.QTextEdit(self.groupBox_2)
        self.txtScale2.setGeometry(QtCore.QRect(610, 540, 81, 31))
        self.txtScale2.setObjectName("txtScale2")
        self.txtScale2.setText("0")

        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(610, 170, 81, 16))
        self.label_11.setObjectName("label_11")
        self.label_11.setText("图像竖直位移")

        self.txtShiftHor2 = QtWidgets.QTextEdit(self.groupBox_2)
        self.txtShiftHor2.setGeometry(QtCore.QRect(610, 260, 81, 31))
        self.txtShiftHor2.setObjectName("txtShiftHor2")
        self.txtShiftHor2.setText("0")

        self.txtShiftVer2 = QtWidgets.QTextEdit(self.groupBox_2)
        self.txtShiftVer2.setGeometry(QtCore.QRect(610, 190, 81, 31))
        self.txtShiftVer2.setObjectName("txtShiftVer2")
        self.txtShiftVer2.setText("0")

        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(610, 280, 79, 72))
        self.label_12.setObjectName("label_12")
        self.label_12.setText("图  像    旋  转")

        self.txtRotation1_2 = QtWidgets.QTextEdit(self.groupBox_2)
        self.txtRotation1_2.setGeometry(QtCore.QRect(610, 330, 81, 31))
        self.txtRotation1_2.setObjectName("txtRotation1_2")
        self.txtRotation1_2.setText("0")

        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(600, 580, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setText("执行操作")
        self.pushButton_2.clicked.connect(self.execution_1)

        self.layoutWidget_3 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget_3.setGeometry(QtCore.QRect(610, 410, 87, 22))
        self.layoutWidget_3.setObjectName("layoutWidget_3")

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.radioBtn2_1_1 = QtWidgets.QRadioButton(self.layoutWidget_3)
        self.radioBtn2_1_1.setObjectName("radioBtn2_1_1")
        self.radioBtn2_1_1.setText("是")
        self.horizontalLayout_4.addWidget(self.radioBtn2_1_1)
        self.radioBtn2_1_0 = QtWidgets.QRadioButton(self.layoutWidget_3)
        self.radioBtn2_1_0.setObjectName("radioBtn2_1_0")
        self.radioBtn2_1_0.setText("否")
        self.radioBtn2_1_0.setChecked(True)
        self.horizontalLayout_4.addWidget(self.radioBtn2_1_0)

        self.layoutWidget_4 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget_4.setGeometry(QtCore.QRect(610, 480, 87, 22))
        self.layoutWidget_4.setObjectName("layoutWidget_4")

        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        self.radioBtn2_2_1 = QtWidgets.QRadioButton(self.layoutWidget_4)
        self.radioBtn2_2_1.setObjectName("radioBtn2_2_1")
        self.radioBtn2_2_1.setText("是")
        self.horizontalLayout_5.addWidget(self.radioBtn2_2_1)
        self.radioBtn2_2_0 = QtWidgets.QRadioButton(self.layoutWidget_4)
        self.radioBtn2_2_0.setObjectName("radioBtn2_2_0")
        self.radioBtn2_2_0.setText("否")
        self.radioBtn2_2_0.setChecked(True)
        self.horizontalLayout_5.addWidget(self.radioBtn2_2_0)

        self.pushBtnExec1_4 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushBtnExec1_4.setGeometry(QtCore.QRect(30, 580, 113, 32))
        self.pushBtnExec1_4.setText("图像取反")
        self.pushBtnExec1_4.setObjectName("pushBtnExec1_4")
        self.pushBtnExec1_4.clicked.connect(self.invert_1)

        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 610, 1501, 481))
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_3.setTitle("图像3")

        self.pushBtnExec1_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushBtnExec1_2.setGeometry(QtCore.QRect(1210, 50, 121, 32))
        self.pushBtnExec1_2.setObjectName("pushBtnExec1_2")
        self.pushBtnExec1_2.setText("执行图像加操作")
        self.pushBtnExec1_2.clicked.connect(self.image_add)

        self.graphicsView_0 = QtWidgets.QGraphicsView(self.groupBox)
        self.graphicsView_0.setGeometry(QtCore.QRect(40, 150, 550, 400))

        self.graphicsView_1 = QtWidgets.QGraphicsView(self.groupBox_2)
        self.graphicsView_1.setGeometry(QtCore.QRect(40, 150, 550, 400))

        self.graphicsView_2 = QtWidgets.QGraphicsView(self.groupBox_3)
        self.graphicsView_2.setGeometry(QtCore.QRect(500, 50, 550, 400))


        QtCore.QMetaObject.connectSlotsByName(Form)

    def select_image_1(self):
        file, file_type = QFileDialog.getOpenFileName(
            parent=None,
            caption="选择图像",
            directory=os.getcwd(),
            filter="bmp文件(*.bmp)"
        )
        self.textEdit.setText(file)
        img = BMP(file)

        # 在QgraphicsScene上呈现检测结果图
        image = img.bmp_data

        #image = image.astype(np.int8)

        self.image_0 = img
        showImage = QtGui.QImage(image.astype(np.int8), image.shape[1], image.shape[0], QtGui.QImage.Format_RGB888)
        pix = QtGui.QPixmap.fromImage(showImage)
        item = QGraphicsPixmapItem(pix)  # 创建像素图元

        scene = QGraphicsScene()  # 创建场景
        scene.addItem(item)
        self.graphicsView_0.setScene(scene)  # 将场景添加至视图

    def select_image_2(self):
        file, file_type = QFileDialog.getOpenFileName(
            parent=None,
            caption="选择图像",
            directory=os.getcwd(),
            filter="bmp文件(*.bmp)"
        )
        self.textEdit_2.setText(file)
        img = BMP(file)
        image = img.bmp_data

        #image = image.astype(np.int8)
        self.image_1 = img

        showImage = QtGui.QImage(image.astype(np.int8), image.shape[1], image.shape[0], QtGui.QImage.Format_RGB888)
        pix = QtGui.QPixmap.fromImage(showImage)
        item = QGraphicsPixmapItem(pix)  # 创建像素图元

        scene = QGraphicsScene()  # 创建场景
        scene.addItem(item)
        self.graphicsView_1.setScene(scene)  # 将场景添加至视图



    def show_processed_image(self, img, area):
        img = img.astype(np.int8)
        showImage = QtGui.QImage(img, img.shape[1], img.shape[0], QtGui.QImage.Format_RGB888)
        pix = QtGui.QPixmap.fromImage(showImage)
        item = QGraphicsPixmapItem(pix)  # 创建像素图元

        scene = QGraphicsScene()  # 创建场景
        scene.addItem(item)
        if area == 0:
            self.graphicsView_0.setScene(scene)  # 将场景添加至视图
        elif area ==1:
            self.graphicsView_1.setScene(scene)
        elif area == 2:
            self.graphicsView_2.setScene(scene)



    def execution_0(self):
        if  self.textEdit.toPlainText():
            # 水平位移
            vertical_shift = float(self.txtShitfVer1.toPlainText())

            # 竖直位移
            horizontal_shift = float(self.txtShiftHor1.toPlainText())

            # 图像旋转
            rotation = float(self.txtRotation1.toPlainText())

            # 图像缩放
            scale = float(self.txtScale1.toPlainText())

            # 是否水平镜像
            is_mirror_horizontal = False

            # 是否竖直镜像
            is_mirror_vertical = False


            if self.radioBtn1_1_1.isChecked():
                is_mirror_horizontal = True
            if self.radioBtn1_2_1.isChecked():
                is_mirror_vertical = True
            #print(self.image_0.bmp_data)


            # 执行位移操作（水平位移和竖直位移）
            if not (vertical_shift == 0  and horizontal_shift == 0):
                self.image_0.shift(vertical_shift, horizontal_shift)

            # 执行旋转操作
            if rotation != 0:
                self.image_0.rotation(rotation)

            # 执行水平镜像操作
            if is_mirror_horizontal == True:
                self.image_0.mirror_horizontal()

            # 执行竖直镜像操作
            if is_mirror_vertical == True:
                self.image_0.mirror_vertical()

            # 图像缩放
            if scale != 0 and scale != 1:
                self.image_0.resize_image(scale)


            self.show_processed_image(self.image_0.bmp_data, 0)

    def execution_1(self):
        if self.textEdit_2.toPlainText():

            # 水平位移
            vertical_shift = float(self.txtShiftVer2.toPlainText())

            # 竖直位移
            horizontal_shift = float(self.txtShiftHor1.toPlainText())

            # 图像旋转
            rotation = float(self.txtRotation1_2.toPlainText())

            # 图像缩放
            scale = float(self.txtScale2.toPlainText())

            # 是否水平镜像
            is_mirror_horizontal = False

            # 是否竖直镜像
            is_mirror_vertical = False

            if self.radioBtn2_1_1.isChecked():
                is_mirror_horizontal = True
            if self.radioBtn2_2_1.isChecked():
                is_mirror_vertical = True

            # 执行旋转操作
            if rotation != 0:
                self.image_1.rotation(rotation)

            # 执行图像位移
            if not (vertical_shift == 0 and horizontal_shift == 0):
                self.image_1.shift(horizontal_shift, vertical_shift)

            # 执行水平镜像操作
            if is_mirror_horizontal == True:
                self.image_1.mirror_horizontal()

            # 执行竖直镜像操作
            if is_mirror_vertical == True:
                self.image_1.mirror_vertical()

            # 执行图像缩放
            if scale != 0 and scale != 1:
                self.image_1.resize_image(scale)

            self.show_processed_image(self.image_1.bmp_data, 1)


    def image_add(self):
            if self.textEdit.toPlainText() and self.textEdit_2.toPlainText():
                img_0 = self.image_0.bmp_data
                img_1 = self.image_1.bmp_data


                if img_0.shape[0] == img_1.shape[0] and img_1.shape[1] == img_1.shape[1]:

                    new_image = np.zeros((img_0.shape[0], img_0.shape[1], 3), dtype=np.int64)


                    for i in range(img_0.shape[0]):
                        for j in range(img_1.shape[1]):

                            new_image[i][j] = 0.5 * img_0[i][j] + 0.5 * img_1[i][j]

                    self.show_processed_image(new_image, 2)
                else:
                    raise ValueError("两张图片的尺寸不同")

    def invert_0(self):
        if self.textEdit.toPlainText():

            self.image_0.invert()
            self.show_processed_image(self.image_0.bmp_data, 0)


    def invert_1(self):
        if self.textEdit_2.toPlainText():
            self.image_1.invert()
            self.show_processed_image(self.image_1.bmp_data, 1)
















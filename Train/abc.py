import tensorflow
from keras.preprocessing.image import img_to_array
from keras.models import model_from_json
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import (QPushButton, QMainWindow, QWidget, QHBoxLayout, QTextEdit,
                             QLabel, QApplication, QLineEdit, QGridLayout, QSlider, QFileDialog)
from PyQt5.QtCore import pyqtSlot, QFileInfo, Qt
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5 import QtGui
from matplotlib import pyplot as plt
import os
import cv2
import numpy as np

import sys

from tkinter import filedialog
from tkinter import *

"""
lineEdit :
    linepath 
Button:
    open

QWidget:
    hinh1
    hinh2 


"""


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()

        ui = uic.loadUi('./system/mainwindow.ui', self)

        li = ui.open.clicked.connect(self.pushOpen)

        showanh_button = ui.showanh.clicked.connect(self.showanh_click)
        run_button = ui.run.clicked.connect(self.run_click)


        self.widget_1 = ui.anhgoc
        self.label = QLabel(self.widget_1)

        self.widget_2 = ui.anhketqua
        self.label_2 = QLabel(self.widget_2)

        img = QImage('./system/white.png')
        pixmap = QPixmap.fromImage(img)
        self.label.setPixmap(pixmap)
        self.label_2.setPixmap(pixmap)
        self.show()

    def pushOpen(self):
        root = Tk()
        root.withdraw()
        root.filename = filedialog.askopenfilename(initialdir="F:/Hoc\DangHoc/NLN/linhtinh", title="Chọn file ảnh",
                                                   filetypes=(("jpeg files", ".jpg"), ("all files", ".*")))
        self.linepath.setText(root.filename)
        print(root.filename)
        root.destroy()

    def showanh_click(self):
        img_show = cv2.imread(self.linepath.text())
        cv2.imwrite('original.jpg', img_show)
        img2 = QImage('original.jpg')
        pixmap = QPixmap.fromImage(img2)
        #img_resize = cv2.resize(pixmap, (128, 128))
        self.label.setPixmap(pixmap)
    def run_click(self):
        # Load model
        json_file = open("F:/Hoc/DangHoc/NLN/NBN/model/model.json", "r")
        json_string = json_file.read()
        json_file.close()
        model = model_from_json(json_string)
        model.load_weights("F:/Hoc/DangHoc/NLN/NBN/model/weights.49.h5")
        names = ["0", "1"]
        #du doan
        img2 = QImage('original.jpg')
        img = cv2.resize(img2, (128, 128))
        img_arr = img_to_array(img) / 255
        img_arr = img_arr.reshape((1,) + img_arr.shape)

        prediction = model.predict(img_arr)[0]
        pos = np.argmax(prediction)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    sys.exit(app.exec_())

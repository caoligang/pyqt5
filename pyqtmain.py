import sys
import RMMainwindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtCore import pyqtSlot, QDir, Qt

import os
from osgeo import gdal
from osgeo import ogr
import numpy as np
import matplotlib.pyplot as plt

import cv2


# 显示遥感图像

def showmap():
    filename = OpenFile_clicked()
    if filename:
        filepath = ''.join(filename)
        img = cv2.imread(filepath,-1)
        cv2.imshow("image", img)
        print(img.min())
        print(img.max())
        cv2.waitKey(0)
        cv2.destroyWindow('image')
    # cv2.destroyAllWindows()


#水体NDWI识别
def waterNDWI():
    filename = OpenFile_clicked()
    if filename:
        filepath = ''.join(filename)
        img = cv2.imread(filepath, -1)
        cv2.imshow("image", img)
        print(img.min())
        print(img.max())
        cv2.waitKey(0)
        cv2.destroyWindow('image')

# 读取遥感数据
def readdata():
    filename = OpenFile_clicked()
    if filename:
        filePath = ''.join(filename)
        ds = gdal.Open(filePath)
        num_bands = ds.RasterCount
        print(num_bands)
        dir(ds)
        print(ds.GetMetadata())
        print(ds.RasterCount)

#显示遥感数据
def showdata():
    filename=OpenFile_clicked()
    if filename:
        filepath=''.join(filename)


# openfile 菜单响应函数
def OpenFile_clicked():
    curPath = QDir.currentPath()
    dlgTitle = "select a file"
    filt = "allfile(*.*);;tiffile(*.tif)"
    filename, fileUsed = QFileDialog.getOpenFileNames(None, dlgTitle, curPath, filt)
    if filename:
        return filename
    else:
        return 0



if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = QMainWindow()
    ui = RMMainwindow.Ui_MainWindow()
    ui.setupUi(mainWin)
    mainWin.show()
    #    readdata()
    ui.actionOpen_File.triggered.connect(readdata)
    ui.actionView_Data.triggered.connect(showdata)
    ui.actionShow_Map.triggered.connect(showmap)
    ui.actionNDWI.triggered.connect(waterNDWI)
    ui.actionOpen_File.tr
    sys.exit(app.exec_())

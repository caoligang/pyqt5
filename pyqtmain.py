import sys
import mainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
import os
from osgeo import gdal
from osgeo import ogr
import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = QMainWindow()
    ui = mainWindow.Ui_MainWindow()
    ui.setupUi(mainWin)
    mainWin.show()
    sys.exit(app.exec_())

'''filePath=r'/Users/caoligang/remote/110000BJ_L5_TM_1990.tif'
ds=gdal.Open(filePath)
dir(ds)
print(ds.GetMetadata())
print(ds.RasterCount)
'''

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RMMainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuWater = QtWidgets.QMenu(self.menubar)
        self.menuWater.setObjectName("menuWater")
        self.menuDeep_Learning = QtWidgets.QMenu(self.menubar)
        self.menuDeep_Learning.setObjectName("menuDeep_Learning")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_File = QtWidgets.QAction(MainWindow)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.actionView_Data = QtWidgets.QAction(MainWindow)
        self.actionView_Data.setObjectName("actionView_Data")
        self.actionNew_File = QtWidgets.QAction(MainWindow)
        self.actionNew_File.setObjectName("actionNew_File")
        self.actionShow_Map = QtWidgets.QAction(MainWindow)
        self.actionShow_Map.setObjectName("actionShow_Map")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionNDWI = QtWidgets.QAction(MainWindow)
        self.actionNDWI.setObjectName("actionNDWI")
        self.menuEdit.addAction(self.actionView_Data)
        self.menuEdit.addAction(self.actionShow_Map)
        self.menuFile.addAction(self.actionOpen_File)
        self.menuFile.addAction(self.actionNew_File)
        self.menuFile.addAction(self.actionClose)
        self.menuWater.addAction(self.actionNDWI)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuWater.menuAction())
        self.menubar.addAction(self.menuDeep_Learning.menuAction())

        self.retranslateUi(MainWindow)
        self.actionClose.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuWater.setTitle(_translate("MainWindow", "water"))
        self.menuDeep_Learning.setTitle(_translate("MainWindow", "Deep Learning"))
        self.actionOpen_File.setText(_translate("MainWindow", "Open File"))
        self.actionView_Data.setText(_translate("MainWindow", "View Data"))
        self.actionNew_File.setText(_translate("MainWindow", "New File"))
        self.actionShow_Map.setText(_translate("MainWindow", "Show Map"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionNDWI.setText(_translate("MainWindow", "NDWI"))

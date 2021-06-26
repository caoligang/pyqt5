import sys
import mainWindow
from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ =="__main__":
    app =QApplication(sys.argv)
    mainwin=QMainWindow()
    ui=mainWindow.Ui_MainWindow()
    ui.setupUi(mainwin)
    mainwin.show()

    sys.exit(app.exec_())
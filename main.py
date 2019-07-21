import sys
import newmainwindow

from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    #Dialog = QDialog()
    Window = QMainWindow()

    ui = newmainwindow.Ui_MainWindow()
    ui.setupUi(Window)

    Window.show()
    sys.exit(app.exec_())
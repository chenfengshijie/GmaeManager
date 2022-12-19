# -*- coding: utf-8 -*-

from GameManagerServer import TransFile
from GameManager import GameManager
from GameManager_ui import Ui_MainWindow
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import pyqtSlot

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)
        self.game_manager = GameManager("setting.json")


        # 绑定信号
        self.pushButton.clicked.connect(self.verify_password)


    def verify_password(self):
        password = self.lineEdit_3.text()
        if password == self.game_manager.password:
            self.lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
            self.lineEdit_2.setFocusPolicy(QtCore.Qt.StrongFocus)
            QMessageBox.information(self.menubar, "提示", "你可以修改设置了", QMessageBox.Cancel, QMessageBox.Cancel)
        else:
            QMessageBox.warning(self.menubar, "警告", "密码错误", QMessageBox.Cancel, QMessageBox.Cancel)
            self.lineEdit.clear()


if __name__ =="__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
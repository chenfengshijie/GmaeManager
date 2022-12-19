# -*- coding: utf-8 -*-
import json

from GameManagerServer import TransFile
from GameManager import GameManager
from GameManager_ui import Ui_MainWindow
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QDateTime, QTimer


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)
        self.game_manager = GameManager("setting.json")
        self.lineEdit_4.setText(str(self.game_manager.used_time))
        self.flush_time = 2000

        self.timer_init()
        # 绑定信号
        self.pushButton.clicked.connect(self.verify_password)
        self.pushButton_2.clicked.connect(self.modify_setting)

    def verify_password(self):
        password = self.lineEdit_3.text()
        if password == self.game_manager.password:
            self.lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
            self.lineEdit_2.setFocusPolicy(QtCore.Qt.StrongFocus)
            QMessageBox.information(self.menubar, "提示", "你可以修改设置了", QMessageBox.Cancel, QMessageBox.Cancel)
        else:
            QMessageBox.warning(self.menubar, "警告", "密码错误", QMessageBox.Cancel, QMessageBox.Cancel)
            self.lineEdit.clear()

    def modify_setting(self):
        if self.lineEdit.focusPolicy() == QtCore.Qt.StrongFocus:
            self.game_manager.setting["Setting"]["Time"] = int(self.lineEdit.text())
            self.game_manager.setting["Setting"]["Game"] = self.lineEdit_2.text().split(",")
            with open("setting.json", "w") as f:
                json.dump(self.game_manager.setting, f)

            QMessageBox.information(self.menubar, "提示", "设置修改成功", QMessageBox.Cancel, QMessageBox.Cancel)
        else:
            QMessageBox.information(self.menubar, "提示", "请先输入密码", QMessageBox.Cancel, QMessageBox.Cancel)

    def timer_init(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.modify_time)
        self.timer.start(self.flush_time)

    def modify_time(self):
        self.game_manager.update_time(self.flush_time)
        self.lineEdit_4.setText(str(self.game_manager.used_time))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())

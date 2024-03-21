#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :gui.py
# @Time      :2024/3/21 
# @Author    :SophistGuaPi

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import gui.gui0 as gui0

class gui:
    def __init__(self, monitor, ser):
        self.monitor = monitor
        self.ser = ser
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = gui0.Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        self.ui.pushButton.clicked.connect(self.clicked_pushbutton)
        self.ui.pushButton_2.clicked.connect(self.clicked_pushbutton_2)
        self.ui.pushButton_5.clicked.connect(self.clicked_pushbutton_5)
        self.ui.pushButton_6.clicked.connect(self.clicked_pushbutton_6)
        self.ui.pushButton_4.clicked.connect(self.clicked_pushbutton_4)
        self.ui.pushButton_3.clicked.connect(self.clicked_pushbutton_3)
        self.ui.
        MainWindow.show()
        sys.exit(app.exec_())

    def clicked_pushbutton(self):
        self.monitor.x_axis[0] = 0
        self.ui.pushButton.setChecked(True)
        self.ui.pushButton_2.setChecked(False)

    def clicked_pushbutton_2(self):
        self.monitor.x_axis[0] = 1
        self.ui.pushButton_2.setChecked(True)
        self.ui.pushButton.setChecked(False)

    def clicked_pushbutton_5(self):
        self.monitor.y_axis[0] = 1
        self.ui.pushButton_5.setChecked(True)
        self.ui.pushButton_6.setChecked(False)

    def clicked_pushbutton_6(self):
        self.monitor.y_axis[0] = 0
        self.ui.pushButton_6.setChecked(True)
        self.ui.pushButton_5.setChecked(False)

    def clicked_pushbutton_4(self):
        self.monitor.del_move_x()

    def clicked_pushbutton_3(self):
        self.monitor.del_move_y()



if __name__ == "__main__":
    pass

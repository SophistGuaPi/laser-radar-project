#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :gui.py
# @Time      :2024/3/21 
# @Author    :SophistGuaPi
import time

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import gui.gui0 as gui0
import threading


class gui:
    def __init__(self, monitor, ser):
        self.monitor = monitor
        self.ser = ser

        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = gui0.Ui_MainWindow()
        self.ui.setupUi(MainWindow)

        #记录数据
        # self.pos_x = CircularSequenceQueue()

        #设置槽函数
        self.ui.pushButton.clicked.connect(self.clicked_pushbutton)
        self.ui.pushButton_2.clicked.connect(self.clicked_pushbutton_2)
        self.ui.pushButton_5.clicked.connect(self.clicked_pushbutton_5)
        self.ui.pushButton_6.clicked.connect(self.clicked_pushbutton_6)
        self.ui.pushButton_4.clicked.connect(self.clicked_pushbutton_4)
        self.ui.pushButton_3.clicked.connect(self.clicked_pushbutton_3)
        self.ui.doubleSpinBox_4.valueChanged.connect(self.value_change_spinbox_4)
        self.ui.doubleSpinBox_3.valueChanged.connect(self.value_change_spinbox_3)
        self.monitor.pos_change_x.connect(self.show_pos_x)
        self.monitor.pos_change_y.connect(self.show_pos_y)
        self.ui.pushButton_8.clicked.connect(self.clicked_pushbutton_8)
        self.ui.pushButton_7.clicked.connect(self.clicked_pushbutton_7)
        self.ser.new_measure.connect(self.show_measure)

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
        self.monitor.y_axis[0] = 0
        self.ui.pushButton_5.setChecked(True)
        self.ui.pushButton_6.setChecked(False)

    def clicked_pushbutton_6(self):
        self.monitor.y_axis[0] = 1
        self.ui.pushButton_6.setChecked(True)
        self.ui.pushButton_5.setChecked(False)

    def clicked_pushbutton_4(self):
        self.monitor.del_move_x()
        self.monitor.get_position_x()

    def clicked_pushbutton_3(self):
        self.monitor.del_move_y()
        self.monitor.get_position_y()

    def value_change_spinbox_4(self):
        self.monitor.x_axis[4] = int(self.ui.doubleSpinBox_4.value())

    def value_change_spinbox_3(self):
        self.monitor.y_axis[4] = int(self.ui.doubleSpinBox_3.value())

    def show_pos_x(self):
        self.ui.textEdit.setText(str(self.monitor.Pos_x.value))

    def show_pos_y(self):
        self.ui.textEdit_2.setText(str(self.monitor.Pos_y.value))

    def clicked_pushbutton_8(self):
        def a():
            while 1:
                self.ser.read()
                time.sleep(0.01)

        if self.ui.pushButton_8.isChecked():
            self.t0 = threading.Thread(target=a, daemon=True)
            self.t0.start()
        elif self.t0.is_alive():
            self.ui.pushButton_8.setChecked(True)

    def clicked_pushbutton_7(self):
        try:
            # 主线程中异步写入数据
            self.ser.write_serial()
        except KeyboardInterrupt:
            print("Serial Communication Stopped.")
        finally:
            pass
            # self.ser.thead.join()

    def show_measure(self):
        self.ui.textEdit_3.setText(self.ser.data)


# class CircularSequenceQueue(object):
#     def __init__(self):
#         self.MaxQuenceSize = 50
#         self.Q = [None for i in range(self.MaxQuenceSize)]
#         self.front = 0
#         self.rear = 0
#
#     def CreateCircularSequenceQueue(self, val_list):
#         for val in val_list:
#             self.EnQueue(val)
#
#     def IsEmpty(self):
#         if self.front == self.rear:
#             return True
#         else:
#             return False
#
#     def LengthQueue(self):
#         return (self.rear - self.front + self.MaxQuenceSize) % self.MaxQuenceSize
#
#     def EnQueue(self, e):
#         if (self.rear + 1) % self.MaxQuenceSize == self.front:
#             print('队已满!')
#             self.DeQueue()
#         else:
#             self.Q[self.rear] = e
#             self.rear = (self.rear + 1) % self.MaxQuenceSize
#
#     def DeQueue(self):
#         if self.IsEmpty():
#             print('队为空!')
#             exit()
#         else:
#             e = self.Q[self.front]
#             self.front = (self.front + 1) % self.MaxQuenceSize
#             return e
#
#     def Traverse(self):
#         return self.Q
#         # for index in range(self.LengthQueue()):
#         #     print(self.Q[index], end=' ')
#         # print('')
#
#     def GetHead(self):
#         return self.Q[self.front]


if __name__ == "__main__":
    import os
    os.system("micromamba shell hook --shell fish&&micromamba activate laser_radar&&pyuic5 -o gui0.py gui0.ui")

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :gui.py
# @Time      :2024/3/21 
# @Author    :SophistGuaPi
import time

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import threading

import gui.gui0 as gui0
import gui.plot as plot
import task.task as task

import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


class gui:
    def __init__(self, monitor, ser):
        self.monitor = monitor
        self.ser = ser
        self.task = task.task(monitor, ser)

        self.dfs = []
        self.datalst = []
        self.datalst_3d = []

        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = gui0.Ui_MainWindow()
        self.ui.setupUi(MainWindow)

        # 记录数据
        # self.pos_x = CircularSequenceQueue()

        # 设置槽函数
        self.ui.pushButton.clicked.connect(self.clicked_pushbutton)
        self.ui.pushButton_2.clicked.connect(self.clicked_pushbutton_2)
        self.ui.pushButton_5.clicked.connect(self.clicked_pushbutton_5)
        self.ui.pushButton_6.clicked.connect(self.clicked_pushbutton_6)
        self.ui.pushButton_4.clicked.connect(self.clicked_pushbutton_4)
        self.ui.pushButton_3.clicked.connect(self.clicked_pushbutton_3)
        self.ui.pushButton_9.clicked.connect(self.clicked_pushbutton_9)
        self.ui.pushButton_14.clicked.connect(self.clicked_pushbutton_14)
        self.ui.pushButton_15.clicked.connect(self.clicked_pushbutton_15)
        self.ui.pushButton_12.clicked.connect(self.clicked_pushbutton_12)
        self.ui.pushButton_17.clicked.connect(self.clicked_pushbutton_17)
        self.ui.pushButton_18.clicked.connect(self.clicked_pushbutton_18)
        self.ui.pushButton_10.clicked.connect(self.clicked_pushbutton_10)
        self.ui.pushButton_11.clicked.connect(self.clicked_pushbutton_11)
        self.ui.pushButton_13.clicked.connect(self.clicked_pushbutton_13)
        self.ui.pushButton_16.clicked.connect(self.clicked_pushbutton_4)
        self.ui.pushButton_19.clicked.connect(self.clicked_pushbutton_3)
        self.ui.pushButton_24.clicked.connect(self.clicked_pushbutton)
        self.ui.pushButton_25.clicked.connect(self.clicked_pushbutton_2)
        self.ui.pushButton_26.clicked.connect(self.clicked_pushbutton_5)
        self.ui.pushButton_27.clicked.connect(self.clicked_pushbutton_6)
        self.ui.doubleSpinBox_4.editingFinished.connect(self.value_change_spinbox_4)
        self.ui.doubleSpinBox_3.editingFinished.connect(self.value_change_spinbox_3)
        self.ui.doubleSpinBox_7.editingFinished.connect(self.value_change_spinbox_7)
        self.ui.doubleSpinBox_8.editingFinished.connect(self.value_change_spinbox_8)
        self.ui.doubleSpinBox_13.editingFinished.connect(self.value_change_spinbox_13)
        self.ui.doubleSpinBox_14.editingFinished.connect(self.value_change_spinbox_14)
        self.ui.doubleSpinBox_11.editingFinished.connect(self.value_change_spinbox_11)
        self.ui.doubleSpinBox_15.editingFinished.connect(self.value_change_spinbox_15)
        self.ui.doubleSpinBox_12.editingFinished.connect(self.value_change_spinbox_12)
        self.ui.doubleSpinBox_20.editingFinished.connect(self.value_change_spinbox_20)
        self.ui.doubleSpinBox_5.editingFinished.connect(self.value_change_spinbox_5)
        self.ui.doubleSpinBox_6.editingFinished.connect(self.value_change_spinbox_6)
        self.ui.spinBox_16.editingFinished.connect(self.value_change_spinbox_16)
        self.ui.spinBox_18.editingFinished.connect(self.value_change_spinbox_18)
        self.monitor.pos_change_x.connect(self.show_pos_x)
        self.monitor.pos_change_y.connect(self.show_pos_y)
        self.ui.pushButton_8.clicked.connect(self.clicked_pushbutton_8)
        self.ui.pushButton_7.clicked.connect(self.clicked_pushbutton_7)
        self.ser.new_measure.connect(self.show_measure)
        self.ui.comboBox.currentTextChanged.connect(self.combobox_change)
        self.ui.comboBox_2.currentTextChanged.connect(self.combobox_change_2)
        self.task.complete_line_scan.connect(self.save_line_data)

        MainWindow.show()
        sys.exit(app.exec_())

    def clicked_pushbutton(self):
        self.monitor.x_axis[0] = 0
        self.ui.pushButton.setChecked(True)
        self.ui.pushButton_2.setChecked(False)
        self.ui.pushButton_24.setChecked(True)
        self.ui.pushButton_25.setChecked(False)

    def clicked_pushbutton_2(self):
        self.monitor.x_axis[0] = 1
        self.ui.pushButton_2.setChecked(True)
        self.ui.pushButton.setChecked(False)
        self.ui.pushButton_25.setChecked(True)
        self.ui.pushButton_24.setChecked(False)

    def clicked_pushbutton_5(self):
        self.monitor.y_axis[0] = 0
        self.ui.pushButton_5.setChecked(True)
        self.ui.pushButton_6.setChecked(False)
        self.ui.pushButton_26.setChecked(True)
        self.ui.pushButton_27.setChecked(False)

    def clicked_pushbutton_6(self):
        self.monitor.y_axis[0] = 1
        self.ui.pushButton_6.setChecked(True)
        self.ui.pushButton_5.setChecked(False)
        self.ui.pushButton_27.setChecked(True)
        self.ui.pushButton_26.setChecked(False)

    def clicked_pushbutton_4(self):
        def a():
            self.monitor.del_move_x()
            self.monitor.get_position_x()

        t = threading.Thread(target=a, daemon=True)
        t.start()

    def clicked_pushbutton_3(self):
        def a():
            self.monitor.del_move_y()
            self.monitor.get_position_y()

        t = threading.Thread(target=a, daemon=True)
        t.start()

    def clicked_pushbutton_9(self):
        self.monitor.init_axis()

    def clicked_pushbutton_14(self):
        def a():
            self.monitor.move_origen()

        t = threading.Thread(target=a, daemon=True)
        t.start()

    def clicked_pushbutton_12(self):
        self.monitor.init_axis()

    def clicked_pushbutton_17(self):
        self.datalst = []
        self.monitor.x_axis[0] = 0
        self.monitor.y_axis[0] = 0

        def a():
            if self.ui.comboBox_3.currentText() == "扫描x":
                self.task.scan_line_x()
            elif self.ui.comboBox_3.currentText() == "扫描y":
                self.task.scan_line_y()
            elif self.ui.comboBox_3.currentText() == "扫描区域（场扫描）":
                self.task.field_scan()

            self.monitor.get_position_x()
            self.monitor.get_position_y()

        t = threading.Thread(target=a, daemon=True)
        t.start()

    def clicked_pushbutton_18(self):
        if self.task.datalst[0]:
            if self.ui.comboBox_3.currentText() == "扫描区域（场扫描）":

                def plt_mat(lst):
                    # data = np.array(lst)
                    # # Convert each 2D matrix into a Pandas DataFrame
                    # dfs = [pd.DataFrame(x) for x in data]
                    # # Create MultiIndex with 3 levels
                    # indices = pd.MultiIndex.from_product([range(s) for s in data.shape])
                    # # Concatenate all Pandas DataFrames into one large DataFrame
                    # df_final = pd.concat(dfs, keys=indices)

                    F = plot.MyFigure(width=5, height=4, dpi=100)
                    F.fig.suptitle("Figuer")
                    max_depth = max([lst[i][0][j] for i in range(len(lst)) for j in range(len(lst[i][0]))])
                    X = np.array([lst[i][1] for i in range(len(lst))])
                    y = np.linspace(self.monitor.range_y_min, self.monitor.range_y_max, len(lst))
                    _, Y = np.meshgrid(X[0], y)
                    # lst = np.array([lst[i][1] for i in range(len(lst))])
                    R = np.array([lst[i][0] for i in range(len(lst))])
                    z0 = R[0][0]

                    X = np.array([R[i] * np.sin((X[i] * np.pi) / 180) for i in range(len(X))])
                    Y = np.array([R[i] * np.sin((Y[i] * np.pi) / 180) for i in range(len(Y))])
                    Z = np.array(
                        [R[i] * np.cos((X[i] * np.pi) / 180) * np.cos((Y[i] * np.pi) / 180) for i in range(len(R))])

                    ax = F.fig.add_subplot(1, 1, 1, projection="3d")
                    # ax.plot_wireframe(X,Y,lst,rcount = 15,ccount = 15)
                    surf = ax.plot_surface(X, Y, Z, cmap='rainbow')
                    ax.contour(X, Y, Z, offset=max_depth + 0.05, cmap='rainbow')  # 绘制等高线
                    F.fig.colorbar(surf, shrink=0.5, aspect=5)
                    self.ui.gridLayout.addWidget(F, 0, 0)

                def reshape_data(data):  # 将数据按照停止位重塑为二维
                    datalst = [[]]
                    data_len = len(data)
                    line_num = 0
                    for i in range(data_len):
                        if data:
                            a = data.pop(0)
                            # print(a,line_num)
                            datalst[line_num].append(a)
                            if a == 'OK\r\n' and data[1][0] == "D":
                                line_num += 1
                                datalst.append([])
                    return datalst

                def extract_data(reshape_data):
                    datalst = []
                    for j in range(len(reshape_data)):
                        data = [None] * len(reshape_data[j])
                        for i in range(len(data)):
                            if reshape_data[j][i][0] == "D":
                                data[i] = float(reshape_data[j][i][2:7])
                            else:
                                data[i] = None
                        data = list(filter(None, data))
                        datalst.append(
                            [data, list(np.linspace(self.monitor.range_x_min, self.monitor.range_x_max, len(data)))])
                    return datalst

                def fill_data(lst):
                    max_datalen = len(max([lst[i][0] for i in range(len(lst))], key=len))
                    for i in range(len(lst)):
                        lst_len = len(lst[i][0])
                        supplement_len = max_datalen - lst_len
                        if supplement_len:
                            if lst_len / (supplement_len + 1) < 1:
                                j = 0
                                while lst_len / (supplement_len + 1) < 1:
                                    lst_len = len(lst[i][0])
                                    supplement_len = max_datalen - lst_len
                                    if (j + 1) + j > len(lst[i][0]):
                                        j = 0
                                    lst[i][0].insert((j + 1) + j, lst[i][0][(j + 1) + j - 1])
                                    lst[i][1].insert((j + 1) + j, lst[i][1][(j + 1) + j - 1])
                                    j += 1
                            split_len = int(lst_len / (supplement_len + 1))
                        lst_len = len(lst[i][0])
                        supplement_len = max_datalen - lst_len
                        for j in range(supplement_len):
                            lst[i][0].insert(split_len * (j + 1) + j, lst[i][0][split_len * (j + 1) + j - 1])
                            lst[i][1].insert(split_len * (j + 1) + j, lst[i][1][split_len * (j + 1) + j - 1])
                    return lst

                data = reshape_data(self.task.datalst)
                data = extract_data(data)
                print(data)
                while data[0] == [[], []]:
                    data.pop(0)
                data = fill_data(data)
                print(data)
                plt_mat(data)
                print(self.task.time_data)

            else:
                data = [None] * len(self.datalst)
                for i in range(len(data)):
                    if self.datalst[i][0] == "D":
                        data[i] = self.datalst[i][2:7]
                    else:
                        data[i] = None
                x = np.linspace(self.monitor.range_x_min, self.monitor.range_x_max, len(data))
                df = pd.DataFrame()
                df["angel"] = x
                df["distance"] = data
                print(df)
                df.to_excel("./data/data0.xlsx")

    def clicked_pushbutton_15(self):
        def a():
            self.monitor.move_origen()

        t = threading.Thread(target=a, daemon=True)
        t.start()

    def clicked_pushbutton_10(self):
        self.ser.mode = "open"
        self.ser.write_serial()
        self.ser.read()

    def clicked_pushbutton_11(self):
        self.monitor.init_axis()

    def clicked_pushbutton_13(self):
        self.ui.doubleSpinBox_14.setValue(self.monitor.Pos_x.value / 1000)
        self.ui.doubleSpinBox_15.setValue(self.monitor.Pos_y.value / 1000 * 0.714286)
        self.value_change_spinbox_14()
        self.value_change_spinbox_15()
        self.ser.mode = "close"
        self.ser.write_serial()
        self.clicked_pushbutton_15()

    def value_change_spinbox_4(self):
        self.monitor.x_axis[4] = int(self.ui.doubleSpinBox_4.value() * 1000)
        self.ui.doubleSpinBox_5.setValue(self.ui.doubleSpinBox_4.value())

    def value_change_spinbox_3(self):
        self.monitor.y_axis[4] = int(self.ui.doubleSpinBox_3.value() * (1000 / 0.714286))
        self.ui.doubleSpinBox_6.setValue(self.ui.doubleSpinBox_3.value())

    def value_change_spinbox_5(self):
        self.monitor.x_axis[4] = int(self.ui.doubleSpinBox_5.value() * 1000)
        self.ui.doubleSpinBox_4.setValue(self.ui.doubleSpinBox_5.value())

    def value_change_spinbox_6(self):
        self.monitor.y_axis[4] = int(self.ui.doubleSpinBox_6.value() * (1000 / 0.714286))
        self.ui.doubleSpinBox_3.setValue(self.ui.doubleSpinBox_6.value())

    def value_change_spinbox_7(self):
        self.monitor.x_axis[3] = int(self.ui.doubleSpinBox_7.value() * 1000)
        self.ui.doubleSpinBox_12.setValue(self.ui.doubleSpinBox_7.value())

    def value_change_spinbox_8(self):
        self.monitor.y_axis[3] = int(self.ui.doubleSpinBox_8.value() * (1000 / 0.714286))
        self.ui.doubleSpinBox_20.setValue(self.ui.doubleSpinBox_8.value())

    def value_change_spinbox_12(self):
        self.monitor.x_axis[3] = int(self.ui.doubleSpinBox_12.value() * 1000)
        self.ui.doubleSpinBox_7.setValue(self.ui.doubleSpinBox_12.value())
        self.ui.spinBox_16.setValue(
            int((self.monitor.range_x_max - self.monitor.range_x_min) * self.ser.frequent * 1000 / self.monitor.x_axis[
                3]))
        self.ser.times_x = self.ui.spinBox_16.value()

    def value_change_spinbox_20(self):
        self.monitor.y_axis[3] = int(self.ui.doubleSpinBox_20.value() * (1000 / 0.714286))
        self.ui.doubleSpinBox_8.setValue(self.ui.doubleSpinBox_20.value())
        self.ui.spinBox_18.setValue(
            int((self.monitor.range_y_max - self.monitor.range_y_min) * self.ser.frequent * 1000 / (
                    self.monitor.y_axis[3] / 0.714286)))
        self.ser.times_y = self.ui.spinBox_18.value()

    def value_change_spinbox_13(self):
        self.monitor.range_x_min = self.ui.doubleSpinBox_13.value()
        self.ui.spinBox_16.setValue(
            int((self.monitor.range_x_max - self.monitor.range_x_min) * self.ser.frequent * 1000 / self.monitor.x_axis[
                3]))
        self.ser.times_x = self.ui.spinBox_16.value()

    def value_change_spinbox_14(self):
        self.monitor.range_x_max = self.ui.doubleSpinBox_14.value()
        self.ui.spinBox_16.setValue(
            int((self.monitor.range_x_max - self.monitor.range_x_min) * self.ser.frequent * 1000 / self.monitor.x_axis[
                3]))
        self.ui.doubleSpinBox_4.setValue(self.ui.doubleSpinBox_14.value() - self.ui.doubleSpinBox_13.value())
        self.ui.doubleSpinBox_5.setValue(self.ui.doubleSpinBox_14.value() - self.ui.doubleSpinBox_13.value())
        self.ser.times_x = self.ui.spinBox_16.value()

    def value_change_spinbox_11(self):
        self.monitor.range_y_min = self.ui.doubleSpinBox_11.value()
        self.ui.spinBox_18.setValue(
            int((self.monitor.range_y_max - self.monitor.range_y_min) * self.ser.frequent * 1000 / (
                    self.monitor.y_axis[3] / 0.714286)))
        self.ser.times_y = self.ui.spinBox_18.value()

    def value_change_spinbox_15(self):
        self.monitor.range_y_max = self.ui.doubleSpinBox_15.value()
        self.ui.spinBox_18.setValue(
            int((self.monitor.range_y_max - self.monitor.range_y_min) * self.ser.frequent * 1000 / (
                    self.monitor.y_axis[3] / 0.714286)))
        self.ui.doubleSpinBox_3.setValue(self.ui.doubleSpinBox_15.value() - self.ui.doubleSpinBox_11.value())
        self.ui.doubleSpinBox_6.setValue(self.ui.doubleSpinBox_15.value() - self.ui.doubleSpinBox_11.value())
        self.ser.times_y = self.ui.spinBox_18.value()

    def value_change_spinbox_16(self):
        pass

    def value_change_spinbox_18(self):
        self.ser.times_y = self.ui.spinBox_18.value()

    def show_pos_x(self):
        self.ui.textEdit.setText(str(self.monitor.Pos_x.value / 1000))
        self.ui.textEdit_4.setText(str(self.monitor.Pos_x.value / 1000))

    def show_pos_y(self):
        self.ui.textEdit_2.setText(str(self.monitor.Pos_y.value * 0.714286 / 1000))
        self.ui.textEdit_5.setText(str(self.monitor.Pos_y.value * 0.714286 / 1000))

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
        self.ui.lineEdit_2.setText(self.ser.data)
        self.datalst.append(self.ser.data)

    def combobox_change(self):
        def a():
            if self.ui.comboBox.currentText() == "单次采样":
                self.ser.mode = "single"
                self.ser.write_serial()
            elif self.ui.comboBox.currentText() == "自动采样":
                self.ser.mode = "auto"
                self.ser.write_serial()
            elif self.ui.comboBox.currentText() == "激光常开":
                self.ser.mode = "open"
                self.ser.write_serial()
            elif self.ui.comboBox.currentText() == "激光常闭":
                self.ser.mode = "close"

        t = threading.Thread(target=a, daemon=True)
        t.start()

    def combobox_change_2(self):
        self.ser.frequent = int(self.ui.comboBox_2.currentText())
        self.ser.init_write()
        self.ui.spinBox_16.setValue(
            int((self.monitor.range_x_max - self.monitor.range_x_min) * self.ser.frequent * 1000 / self.monitor.x_axis[
                3]))
        self.ui.spinBox_18.setValue(
            int((self.monitor.range_y_max - self.monitor.range_y_min) * self.ser.frequent * 1000 / (
                    self.monitor.y_axis[3] / 0.714286)))
        self.ser.times_x = self.ui.spinBox_16.value()
        self.ser.times_y = self.ui.spinBox_18.value()

    def save_line_data(self):
        data = [None] * len(self.datalst)
        for i in range(len(data)):
            if self.datalst[i][0] == "E":
                data[i] = None
            else:
                data[i] = self.datalst[i][2:7]
        x = np.linspace(self.monitor.range_x_min, self.monitor.range_x_max, len(data))
        lst = [data, x]
        self.dfs.append(lst)


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

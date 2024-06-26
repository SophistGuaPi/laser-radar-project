# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testplot.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

matplotlib.use("Qt5Agg")


class MyFigure(FigureCanvas):
    def __init__(self, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        super(MyFigure, self).__init__(self.fig)



        # data = np.array(lst)
        # # Convert each 2D matrix into a Pandas DataFrame
        # dfs = [pd.DataFrame(x) for x in data]
        # # Create MultiIndex with 3 levels
        # indices = pd.MultiIndex.from_product([range(s) for s in data.shape])
        # # Concatenate all Pandas DataFrames into one large DataFrame
        # df_final = pd.concat(dfs, keys=indices)




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 30, 691, 491))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # self.F = MyFigure(width=10, height=6, dpi=100)
        # # self.groupBox = QGroupBox(self.plt3d_module)
        # self.gridLayout.addWidget(self.F, 0, 0)

        lst = [[[1.764, 1.766, 1.766, 1.772, 1.774, 1.774, 1.779, 1.774, 1.771, 1.781, 1.778, 1.778, 1.778, 1.781,
                 1.792, 1.782],
                [0.0, 0.06666666666666667, 0.13333333333333333, 0.2, 0.26666666666666666, 0.3333333333333333, 0.4,
                 0.4666666666666667, 0.5333333333333333, 0.6, 0.6666666666666666, 0.7333333333333333, 0.8,
                 0.8666666666666667, 0.9333333333333333, 1.0]], [
                   [1.774, 1.772, 1.772, 1.772, 1.77, 1.77, 1.773, 1.773, 1.774, 1.778, 1.78, 1.778, 1.78, 1.78, 1.785,
                    1.785], [0.0, 0.07142857142857142, 0.14285714285714285, 0.21428571428571427, 0.2857142857142857,
                             0.3571428571428571, 0.42857142857142855, 0.42857142857142855, 0.5, 0.5714285714285714,
                             0.6428571428571428, 0.7142857142857142, 0.7857142857142857, 0.8571428571428571,
                             0.9285714285714285, 1.0]], [
                   [1.774, 1.771, 1.77, 1.77, 1.77, 1.768, 1.772, 1.774, 1.774, 1.778, 1.773, 1.779, 1.779, 1.779,
                    1.783, 1.778],
                   [0.0, 0.07692307692307693, 0.15384615384615385, 0.23076923076923078, 0.23076923076923078,
                    0.3076923076923077, 0.38461538461538464, 0.46153846153846156, 0.46153846153846156,
                    0.5384615384615385, 0.6153846153846154, 0.6923076923076923, 0.7692307692307693, 0.8461538461538463,
                    0.9230769230769231, 1.0]]]

        F1 = MyFigure(width=5, height=4, dpi=100)
        F1.fig.suptitle("Figuer_4")
        X = np.array([lst[i][1] for i in range(len(lst))])
        y = np.linspace(0, 1, len(lst))
        _, Y = np.meshgrid(X[0], y)
        # lst = np.array([lst[i][1] for i in range(len(lst))])
        lst = np.array([lst[i][0] for i in range(len(lst))])
        ax = F1.fig.add_subplot(1, 1, 1, projection="3d")
        # ax.plot_wireframe(X,Y,lst,rcount = 15,ccount = 15)
        surf = ax.plot_surface(X, Y, lst, cmap='rainbow')
        ax.contour(X, Y, lst, offset=-2, cmap='rainbow')  # 绘制等高线
        F1.fig.colorbar(surf, shrink=0.5, aspect=5)

        self.gridLayout.addWidget(F1, 0, 0)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

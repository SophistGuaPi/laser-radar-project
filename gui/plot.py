#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :plot.py
# @Time      :2024/4/9 
# @Author    :SophistGuaPi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib

matplotlib.use("Qt5Agg")


class MyFigure(FigureCanvas):
    def __init__(self, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        super(MyFigure, self).__init__(self.fig)


if __name__ == "__main__":
    pass

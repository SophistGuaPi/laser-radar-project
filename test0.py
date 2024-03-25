#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :test0.py
# @Time      :2024/3/25 
# @Author    :SophistGuaPi

import laser_measurement.measurement as measurement
import monitor.monitor as monitor
import threading
import time
import gui.gui as gui
import sys
from PyQt5 import QtCore, QtGui, QtWidgets


if __name__ == "__main__":
    # 串口参数
    port = '/dev/ttyUSB0'  # 串口设备路径

    # 打开串口
    ser = measurement.measure(port)
    monitor = monitor.monitor()

    # 初始化激光器
    ser.init_write(20)
    ser.mode = "singgel"

    # 启动GUI
    gui = gui.gui(monitor, ser)

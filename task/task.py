#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :task.py
# @Time      :2024/3/26 
# @Author    :SophistGuaPi

import monitor.monitor as monitor
import laser_measurement.measurement as measurement
import threading
import time
from PyQt5 import QtCore, QtGui, QtWidgets


class task(QtCore.QObject):
    complete_line_scan = QtCore.pyqtSignal()

    def __init__(self, monitor, ser):
        super().__init__()
        self.monitor = monitor
        self.ser = ser
        self.datalst = []
        self.data = []
        self.stop_x = False
        self.times_y = 0
        self.destination_x = 0
        self.destination_y = 0

        #统计数据
        self.rank = 0
        self.line_times = 0
        self.start_time = time.perf_counter()
        self.end_time = 0
        self.time_data = []

    def scan_line_x(self):
        self.rank += 1
        self.line_times = 0
        self.start_time = time.perf_counter()
        t = []

        def mov():
            self.monitor.del_move_x()
            self.monitor.get_position_x()

        def measure():
            def read():
                self.stop_x = True
                while self.destination_x > self.monitor.Pos_x.value + 1:
                    self.data.append(self.ser.read())
                    # self.data.append([self.ser.read(), self.monitor.Pos_x.value])

                    self.line_times += 1
                    t.append(time.perf_counter() - self.start_time)
                else:
                    self.ser.stop_auto()

            self.ser.mode = "fast auto"
            try:
                self.ser.write_serial()
            except KeyboardInterrupt:
                print("Serial Communication Stopped.")

            self.stop_x = True
            t0 = threading.Thread(target=read, daemon=True)
            t0.start()

        def stop():
            self.stop_x = False
            self.ser.stop_auto()

        self.monitor.monitor_stop_x.connect(stop)
        self.monitor.x_axis[4] = int((self.monitor.range_x_max - self.monitor.range_x_min) * 1000)
        self.destination_x = self.monitor.Pos_x.value + self.monitor.x_axis[4]

        t1 = threading.Thread(target=mov, daemon=True)
        t2 = threading.Thread(target=measure, daemon=True)
        t1.start()
        t2.start()

        self.time_data.append(t)

    def scan_line_y(self):
        def mov():
            self.monitor.y_axis[4] = int((self.monitor.range_y_max - self.monitor.range_y_min) * 1000 / 0.714286)
            self.monitor.del_move_y()

        def measure():
            def read():
                self.stop_y = True
                while self.stop_y:
                    self.ser.read()

            self.ser.mode = "fast auto"
            try:
                self.ser.write_serial()
            except KeyboardInterrupt:
                print("Serial Communication Stopped.")

            self.stop_y = True
            t0 = threading.Thread(target=read, daemon=True)
            t0.start()

        def stop():
            self.stop_y = False
            self.ser.stop_auto()

        self.monitor.monitor_stop_y.connect(stop)

        t1 = threading.Thread(target=mov, daemon=True)
        t2 = threading.Thread(target=measure, daemon=True)
        t1.start()
        t2.start()

    def field_scan(self):
        lock = threading.RLock()
        def scan():
            # while self.times_y <= 2:
            lock.acquire()
            # print(self.times_y)
            self.scan_line_x()
            lock.acquire(False)

        def next_row():
            # while self.times_y <= 2:
            lock.acquire()
            self.monitor.x_axis[0] = 1
            self.monitor.x_axis[4] = int((self.monitor.range_x_max - self.monitor.range_x_min) * 1000)
            self.monitor.x_axis[3] = 10000
            self.monitor.del_move_x()
            self.monitor.get_position_x()
            self.monitor.x_axis[0] = 0
            self.monitor.x_axis[3] = speed

            self.monitor.y_axis[4] = int(((self.monitor.range_y_max-self.monitor.range_y_min) / self.ser.times_y) * (1000 / 0.714286))
            self.monitor.del_move_y()
            self.monitor.get_position_y()

            self.monitor.get_position_x()
            self.monitor.get_position_y()

            self.datalst += self.data
            self.data = []

            self.complete_line_scan.emit()
            lock.acquire(False)

        speed = self.monitor.x_axis[3]
        for i in range(self.ser.times_y):
            scan()
            # self.datalst.append(self.data)
            while self.destination_x != self.monitor.Pos_x.value:
                time.sleep(0.01)
            time.sleep(1.3)
            next_row()
            time.sleep(0.2)



if __name__ == "__main__":
    pass

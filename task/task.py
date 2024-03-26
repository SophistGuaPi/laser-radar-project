#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :task.py
# @Time      :2024/3/26 
# @Author    :SophistGuaPi

import monitor.monitor as monitor
import laser_measurement.measurement as measurement
import threading
import time


class task:
    def __init__(self, monitor, ser):
        self.monitor = monitor
        self.ser = ser
        self.data = []

    def scan_line_x(self):
        def mov():
            self.monitor.x_axis[4] = int((self.monitor.range_x_max - self.monitor.range_x_min) * 1000)
            self.monitor.del_move_x()

        def measure():
            while 1:
                self.ser.read_serial()
                time.sleep(self.ser.frequent)
                print(self.ser.data)

        t0 = threading.Thread(target=mov, daemon=True)
        t1 = threading.Thread(target=measure, daemon=True)
        t0.start()
        t1.start()
        t1.join()



if __name__ == "__main__":
    pass

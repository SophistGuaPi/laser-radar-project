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
        self.datalst = []
        self.stop_x = False

    def scan_line_x(self):
        def mov():
            self.monitor.x_axis[4] = int((self.monitor.range_x_max - self.monitor.range_x_min) * 1000)
            self.monitor.del_move_x()

        def measure():
            def read():
                self.stop_x = True
                while self.stop_x:
                    self.ser.read()

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

        t1 = threading.Thread(target=mov, daemon=True)
        t2 = threading.Thread(target=measure, daemon=True)
        t1.start()
        t2.start()



if __name__ == "__main__":
    pass

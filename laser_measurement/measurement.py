#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :measurement.py
# @Time      :2024/3/5 
# @Author    :SophistGuaPi

import serial
import threading
import time

class measure:
    def __init__(self, port):
        self.mode = "singgel"
        baudrate = 115200  # 波特率
        timeout = 1  # 超时时间（秒）
        bytesize = serial.EIGHTBITS  # 数据位
        stopbits = serial.STOPBITS_ONE  # 停止位
        self.ser = serial.Serial(port, baudrate, bytesize, stopbits=stopbits, timeout=timeout)
        self.data = None


        # 异步读取数据的线程函数
    def read_serial(self):
        def read():
            while True:
                data = self.ser.readline()
                if data:
                    self.data = data
                    print(self.data.decode('utf-8'))
                    break

        # 创建并运行线程
        self.thread = threading.Thread(target=read)
        self.thread.start()

        try:
            # 主线程中异步写入数据
            self.write_serial()
        except KeyboardInterrupt:
            print("Serial Communication Stopped.")
        finally:
            self.thread.join()


    def init_write(self, samp_rate):
        self.ser.write((f"iSET:7,{samp_rate}\r\n").encode())
        print(self.ser.readline().decode('utf-8'))

    def write_serial(self):
        if self.mode == "singgel":
            self.ser.write(f"iSM\r\n".encode())
        if self.mode == "auto":
            self.ser.write(f"iACM\r\n".encode())
        if self.mode == "fast auto":
            self.ser.write(f"iFACM\r\n".encode())

    def stop_serial(self):

        if self.ser.is_open:
            self.ser.write((f"iHALT\r\n").encode())
            self.ser.close()





if __name__ == "__main__":
    pass

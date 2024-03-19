#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :monitor.py
# @Time      :2024/3/6 
# @Author    :SophistGuaPi
import time
from ctypes import *

class monitor:
    def __init__(self):
        CDLL('libusb-1.0.so', RTLD_GLOBAL)
        self.DAQdll = cdll.LoadLibrary('example/LibUSB_AMC2XE.so')

        # 首先打开设备
        erro = self.DAQdll.OpenUSB_2XE()
        # 初始化x轴
        erro = self.DAQdll.Set_Axs_2XE(0, 0, 0, 0, 0, 0)
        erro = self.DAQdll.Set_Axs_2XE(0, 0, 1, 0, 0, 0)

        # 初始化Y轴
        erro = self.DAQdll.Set_Axs_2XE(0, 1, 0, 0, 0, 0)
        erro = self.DAQdll.Set_Axs_2XE(0, 1, 1, 0, 0, 0)
        self.Pos = c_uint(1)  #
        self.RunState = c_int(1)
        self.IOState = c_char(1)
        self.CEMG = c_char(1)

    def del_move(self, x_axis, y_axis):
        # x轴定长运动,正向运行，直线加减速，初始速度1000脉冲每秒，运行速度5000脉冲每秒，运行距离10000脉冲，加速时间100ms，减速时间100ms
        erro = self.DAQdll.DeltMov_2XE(0, 0, 0, x_axis[0], x_axis[1], x_axis[2], x_axis[3], x_axis[4], x_axis[5], x_axis[6], x_axis[7])
        # y轴定长运动,正向运行，直线加减速，初始速度1000脉冲每秒，运行速度5000脉冲每秒，运行距离10000脉冲，加速时间100ms，减速时间100ms
        erro = self.DAQdll.DeltMov_2XE(0, 1, 0, y_axis[0], y_axis[1], y_axis[2], y_axis[3], y_axis[4], y_axis[5], y_axis[6], y_axis[7])

        # 由于int __stdcall Read_Position_2XE(int dev,unsigned int Axs,unsigned int* Pos,unsigned char* RunState,unsigned char* IOState,unsigned char* CEMG);
        # 函数需要返回很多结果值，使用unsigned int*，unsigned char*传入一个地址，读取结果写入这个指针所指向的地址，
        # 所以需要先申明一个unsigned int，unsigned char类型的变量，然后使用byref得到这个变量地址当做指针传给函数
    def get_position(self):
        # 读取X轴状态
        erro = self.DAQdll.Read_Position_2XE(0, 0, byref(self.Pos), byref(self.RunState), byref(self.IOState),
                                             byref(self.CEMG))
        while self.RunState.value > 0:
            # 打印X轴的逻辑位置
            erro = self.DAQdll.Read_Position_2XE(0, 0, byref(self.Pos), byref(self.RunState), byref(self.IOState),
                                                 byref(self.CEMG))
            print("pos:"+str(self.Pos.value))
            print("RunState:"+str(self.RunState.value))

if __name__ == "__main__":
    pass
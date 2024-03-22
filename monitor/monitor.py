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

        self.Pos_x = c_uint(1)  #
        self.RunState_x = c_int(1)
        self.IOState_x = c_char(1)
        self.CEMG_x = c_char(1)
        self.Pos_y = c_uint(1)  #
        self.RunState_y = c_int(1)
        self.IOState_y = c_char(1)
        self.CEMG_y = c_char(1)

        self.x_axis = [0, 0, 1000, 10000, 1000, 100, 1, 1]
        self.y_axis = [1, 0, 1000, 1000, 50, 100, 1, 1]

    def del_move_x(self):
        # x轴定长运动,正向运行，直线加减速，初始速度1000脉冲每秒，运行速度5000脉冲每秒，运行距离10000脉冲，加速时间100ms，减速时间100ms
        erro = self.DAQdll.DeltMov_2XE(0, 0, 0, self.x_axis[0], self.x_axis[1], self.x_axis[2], self.x_axis[3], self.x_axis[4], self.x_axis[5],
                                       self.x_axis[6], self.x_axis[7])


        # 由于int __stdcall Read_Position_2XE(int dev,unsigned int Axs,unsigned int* Pos_x,unsigned char* RunState_x,unsigned char* IOState_x,unsigned char* CEMG_x);
        # 函数需要返回很多结果值，使用unsigned int*，unsigned char*传入一个地址，读取结果写入这个指针所指向的地址，
        # 所以需要先申明一个unsigned int，unsigned char类型的变量，然后使用byref得到这个变量地址当做指针传给函数

    def del_move_y(self):
        # y轴定长运动,正向运行，直线加减速，初始速度1000脉冲每秒，运行速度5000脉冲每秒，运行距离10000脉冲，加速时间100ms，减速时间100ms
        erro = self.DAQdll.DeltMov_2XE(0, 1, 0, self.y_axis[0], self.y_axis[1], self.y_axis[2], self.y_axis[3],
                                       self.y_axis[4], self.y_axis[5],
                                       self.y_axis[6], self.y_axis[7])

    def get_position_x(self):
        # 读取X轴状态
        erro = self.DAQdll.Read_Position_2XE(0, 0, byref(self.Pos_x), byref(self.RunState_x), byref(self.IOState_x),
                                             byref(self.CEMG_x))
        while self.RunState_x.value > 0:
            # 打印X轴的逻辑位置
            erro = self.DAQdll.Read_Position_2XE(0, 0, byref(self.Pos_x), byref(self.RunState_x), byref(self.IOState_x),
                                                 byref(self.CEMG_x))

    def get_position_y(self):
        # 读取X轴状态
        erro = self.DAQdll.Read_Position_2XE(0, 1, byref(self.Pos_y), byref(self.RunState_y), byref(self.IOState_y),
                                             byref(self.CEMG_y))
        while self.RunState_y.value > 0:
            # 打印X轴的逻辑位置
            erro = self.DAQdll.Read_Position_2XE(0, 1, byref(self.Pos_y), byref(self.RunState_y), byref(self.IOState_y),
                                                 byref(self.CEMG_y))


if __name__ == "__main__":
    pass

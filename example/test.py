from ctypes import *

CDLL('libusb-1.0.so', RTLD_GLOBAL)
DAQdll = cdll.LoadLibrary('./LibUSB_AMC2XE.so')

# 首先打开设备
erro = DAQdll.OpenUSB_2XE()
# 初始化x轴
erro = DAQdll.Set_Axs_2XE(0, 0, 0, 0, 0, 0)
erro = DAQdll.Set_Axs_2XE(0, 0, 1, 0, 0, 0)

# 初始化Y轴
erro = DAQdll.Set_Axs_2XE(0, 1, 0, 0, 0, 0)
erro = DAQdll.Set_Axs_2XE(0, 1, 1, 0, 0, 0)
# x轴定长运动,正向运行，直线加减速，初始速度1000脉冲每秒，运行速度5000脉冲每秒，运行距离10000脉冲，加速时间100ms，减速时间100ms
erro = DAQdll.DeltMov_2XE(0, 0, 0, 0, 0, 1000, 5000, 10000, 0, 100, 100);

# y轴定长运动，反向运行，S曲线线加减速，初始速度1000脉冲每秒，运行速度5000脉冲每秒，运行距离10000脉冲，加速时间100ms，减速时间100ms
erro = DAQdll.DeltMov_2XE(0, 1, 1, 1, 0, 1000, 5000, 10000, 0, 100, 100);

# 由于int __stdcall Read_Position_2XE(int dev,unsigned int Axs,unsigned int* Pos,unsigned char* RunState,unsigned char* IOState,unsigned char* CEMG);

# 函数需要返回很多结果值，使用unsigned int*，unsigned char*传入一个地址，读取结果写入这个指针所指向的地址，
# 所以需要先申明一个unsigned int，unsigned char类型的变量，然后使用byref得到这个变量地址当做指针传给函数
Pos = c_uint(1)  #
RunState = c_int(1)
IOState = c_char(1)
CEMG = c_char(1)
while RunState.value > 0:  # X轴状态停止时的值为0，当读取到运行状态为0 ，表示电机已经运行到指定位置
    # 读取X轴状态
    erro = DAQdll.Read_Position_2XE(0, 0, byref(Pos), byref(RunState), byref(IOState), byref(CEMG))
    # 打印X轴的逻辑位置
    print(Pos.value)
# 最后需要关闭设备
erro = DAQdll.CloseUSB_2XE()

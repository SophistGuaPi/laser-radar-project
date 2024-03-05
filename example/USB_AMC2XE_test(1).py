from ctypes import *

CDLL('libusb-1.0.so', RTLD_GLOBAL)
DAQdll = cdll.LoadLibrary('./LibUSB_AMC2XE.so')
erro = DAQdll.OpenUSB_2XE()
erro = DAQdll.Set_Axs_2XE(0, 0, 0, 0, 0, 0)
erro = DAQdll.Set_Axs_2XE(0, 0, 1, 0, 0, 0)

erro = DAQdll.DeltMov_2XE(0, 0, 0, 1, 0, 1000, 5000, 10000, 0, 100, 100)

erro = DAQdll.CloseUSB_2XE()

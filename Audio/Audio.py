import wave
#  导入 wave 模块
import matplotlib.pyplot as plt # 用于绘制波形图
import numpy as np
import math
# 用于计算波形数据
import os
# 用于系统处理，如读取本地音频文件


"""
一.读取本地音频数据
处理音频第一步是需要从让计算机“听到”声音，这里我们使用 python 标准库中自带的 wave 模块进行音频参数的获取。
（1）	导入 wave 模块
（2）	使用 wave 中的函数 open 打开音频文件，wave.open(file,mode)函数带有两个参数， 第一个 file 是所需要打开的文件名及路径，使用字符串表示；第二个 mode 是打开的模式，也是用字符串表示 （’rb’或’wb’）
（3）	打开音频后使用 getparams() 获取音频基本的相关参数，其中 nchannels:声道数；
sampwidth:量化位数或量化深度（byte）；framerate:采样频率；nframes:采样点数
"""

f = wave.open(r"Data/Drum.wav",'rb' )
params = f.getparams ()
nchannels,sampwidth, framerate, nframes = params [:4]
print(framerate)

"""
二：读取单通道音频，并绘制波形图（常见音频为左右，2个声道） 
（1）	通过第一步，可以继续读取音频数据本身，保存为字符串格式 
strData = f.readframes(nframes)
（2）	如果需要绘制波形图，则需要将字符串格式的音频数据转化为 int 类型 
waveData = np.fromstring(strData,dtype=np.int16)
此处需要使用到 numpy 进行数据格式的转化 
（3）	将幅值归一化 
waveData = waveData*1.0/(max(abs(waveData)))
这一步去掉也可画出波形图，大家可以尝试不用此步，找出波形图的不同 
（4）	绘制图像
time = np.arange(0,nframes)*(1.0 / framerate)#计算音频的时间
plt.plot(time,waveData)
plt.xlabel("Time(s)") 
plt.ylabel("Amplitude")
plt.title("Single channel wavedata") 
plt.show()

"""
strData = f.readframes(nframes)
waveData = np.frombuffer(strData,dtype=np.int16)
waveData = waveData*1.0/(max(abs(waveData)))

time = np.arange(0,nframes)*(1.0 / framerate)#计算音频的时间
#DeBug
#print(len(time))
#print(len(waveData))
"""问题解决： 
raise ValueError(f"x and y must have same first dimension, but "
ValueError: x and y must have same first dimension, but have shapes (112896,) and (225792,)
refer:https://blog.csdn.net/qq_37591637/article/details/102835118
time要和waveData维度要一致
"""

"""
len_waveData = len(time)
waveData = waveData[0:len_waveData]
plt.plot(time,waveData)
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")
plt.title("Single channel wavedata")
plt.show()
"""

"""
三： 多通道语音数据读取 
waveData 多维的矩阵
plt.plot(time,waveData[:,n])#绘制waveData数据的第n列，即音频第n个通道的数据
"""
waveData = np.reshape(waveData,[nframes,nchannels])
f.close()
time = np.arange(0,nframes)*(1.0 / framerate)
plt.figure()
plt.subplot(5,1,1)
plt.plot(time,waveData[:,0])
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")
plt.title("Ch-1 wavedata")
plt.subplot(5,1,3)
plt.plot(time,waveData[:,1])
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")
plt.title("Ch-2 wavedata")
plt.subplot(5,1,5)
plt.plot(time,waveData[:,1])
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")
plt.title("Ch-3 wavedata")
plt.show()

"""
四：语音信号短时能量 
计算较短时间内的语音能量。这里短时指的是一帧（256个采样点）。
"""
def calEnergy(wave_data) :
    energy  =  []
    sum = 0
    frameSize = 256
    for i in range(len(wave_data)) :#计算每一帧的数据和
        sum = sum + (wave_data[i] * wave_data[i])#采样点数据平方
        if (i + 1) % frameSize == 0 :
            energy.append(sum)
            sum = 0
        elif i == len(wave_data) - 1 :
            energy.append(sum)
    return energy

#绘制
energy = calEnergy(waveData[:, 0])
time2 = np.arange(0, len(energy)) * (len(waveData[:, 0]) / len(energy) / framerate)

plt.plot(time2, energy)
plt.ylabel("short energy")
plt.xlabel("time (seconds)")
plt.show()

"""
五：语音信号短时过零率 
在每帧中（256个采样点），语音信号通过零点（从正变为负或从负变为正）的次数。
"""
def ZeroCR(wave_data,frameSize,overLap):
    wlen = len(wave_data)
    step = frameSize - overLap
    frameNum = math.ceil(wlen/step)#帧的数量
    zcr = np.zeros((frameNum,1))
    for i in range(frameNum):#每帧过零的次数计算
        curFrame = wave_data[np.arange(i*step,min(i*step+frameSize,wlen))]
        curFrame = curFrame - np.mean(curFrame)
        zcr[i] = sum(curFrame[0:-1]*curFrame[1::]<=0)
    return zcr


#绘制
frameSize = 256
overLap = 0
zcr = ZeroCR(waveData[:, 0], frameSize, overLap)
Time3 = np.arange(0, len(zcr)) * (len(waveData[:, 0]) / len(zcr) / framerate)

plt.plot(Time3, zcr)
plt.ylabel("ZCR")
plt.xlabel("time (seconds)")
plt.show()

"""
六：绘制语谱图 
"""

"""
宽带
帧长，包含采样点数，必须为2^n，n取小（如32，画出的图为宽带频谱图），n取大（如
2048，画出的图为窄带频谱图） framesize = 32  
计算离散傅里叶变换的点数，NFFT必须与时域的点数framsize相等，即不补零的FFT NFFT = framesize 
设置帧与帧重叠部分采样点数，overlapSize约为每帧点数的1/3~1/2 overlapSize = 1.0 / 3 * framesize   
overlapSize = int(round(overlapSize)) # 取 整 
绘制频谱图 
plt.specgram(waveData[:,0], NFFT=NFFT, Fs=framerate,window=np.hanning(M=framesize), noverlap=overlapSize)  
"""

framesize = 32
NFFT = framesize
overlapSize = 1.0 / 3 * framesize
overlapSize = int(round(overlapSize)) # 取 整
plt.specgram(waveData[:,0], NFFT=NFFT, Fs=framerate,window=np.hanning(M=framesize), noverlap=overlapSize)
#绘制
plt.ylabel('Frequency')
plt.xlabel('Time')
plt.ylim(0, 6000)
plt.title("Wide Band Spectrum")
plt.show()

"""
窄带
"""
framesize = 2048
framelength = framesize / framerate
NFFT = framesize
overlapSize = 1.0 / 3 * framesize
overlapSize = int(round(overlapSize))
plt.specgram(waveData[:,0],
NFFT=NFFT,Fs=framerate,window=np.hanning(M=framesize), noverlap=overlapSize)
plt.ylabel('Frequency')
plt.xlabel('Time')
plt.ylim(0, 6000)
plt.title("Narrow Band Spectrum")
plt.show()

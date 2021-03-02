#练习 3.：FFmpeg 给视频增加滤镜
import subprocess

VideoPath="D:\EVERTHING\\test\\test2.mp4"

# boxblur 滤镜，模糊处理
cmd = "ffmpeg -i "+VideoPath+" -vf	boxblur=4:1 output1.mp4"
subprocess.call(cmd, shell=True)
#添加红色偏色的阴影
cmd = "ffmpeg -i "+VideoPath+" -vf colorbalance=rs=.3 output2.mp4"
subprocess.call(cmd, shell=True)
#混合滤镜，给视频添加 logo
cmd = "ffmpeg -i "+VideoPath+" -i logo.jpg -filter_complex overlay output3.mp4"
subprocess.call(cmd, shell=True)
import os


VedeoPath="D:\EVERTHING\\test\\test.mp4"
#获取视频时长
cmd='ffprobe -i %s -show_entries format=duration -of csv="p=0" -v quiet'%VedeoPath #视频路径
#duration=os.popen(cmd,'r')
duration=os.popen(r'ffprobe -i D:/EVERTHING/test/test.mp4 -show_entries format=duration -of csv="p=0" -v quiet','r')
duration=duration.read()
#print('duration'+duration)
#获取视频帧率
cmd='ffprobe -count_frames -i %s -select_streams v:0 -show_entries stream=avg_frame_rate -of csv="p=0" -v quiet'%VedeoPath#视频路径
rate=os.popen(cmd,'r')
rate=rate.read()

##获取视频帧数
cmd='ffprobe -count_frames -i %s -select_streams v:0 -show_entries stream=nb_read_frames -of csv="p=0" -v quiet'%VedeoPath#视频路径
frames=os.popen(cmd,'r')
frames=frames.read()

#获取视频帧的长度和宽度
cmd1='ffprobe -count_frames -i %s -select_streams v:0 -show_entries stream=height -of csv="p=0" -v quiet'%VedeoPath#视频路径
cmd2='ffprobe -count_frames -i %s -select_streams v:0 -show_entries stream=width -of csv="p=0" -v quiet'%VedeoPath#视频路径
height=os.popen(cmd1,'r')
width=os.popen(cmd2,'r')
height=height.read()
width=width.read()

#读取展示
print('Number of Frames = ', frames[:-1])
print ('Frame Rate = ',rate[:-1],'fps')
print('Duration = ', duration[:-1],'sec')
print('Height = ', height[:-1],'px')
print('Width = ', height[:-1],'px')

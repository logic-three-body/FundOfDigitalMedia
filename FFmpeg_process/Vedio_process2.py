import subprocess
#每秒提取一帧视频帧
VideoPath="D:\EVERTHING\\test\\test2.mp4"
OutputPath = "D:\EVERTHING\\test\keyframes"
cmd = "ffmpeg -i " + VideoPath+" -r 1 -f image2 "+OutputPath+ "\%06d.jpg"
subprocess.call(cmd, shell=True)

#提取 I 帧
OutputPath = "D:\EVERTHING\\test\I_keyframes"
cmd = 'ffmpeg -i '+VideoPath+' -vf "select=eq(pict_type\,I)" -vsync vfr '+OutputPath + '/%06d.jpg'
subprocess.call(cmd, shell=True)

#提取B 帧
OutputPath = "D:\EVERTHING\\test\B_keyframes"
cmd = 'ffmpeg -i '+VideoPath+' -vf "select=eq(pict_type\,B)" -vsync vfr '+OutputPath + '/%06d.jpg'
subprocess.call(cmd, shell=True)

#提取P 帧
OutputPath = "D:\EVERTHING\\test\P_keyframes"
cmd = 'ffmpeg -i '+VideoPath+' -vf "select=eq(pict_type\,P)" -vsync vfr '+OutputPath + '/%06d.jpg'
subprocess.call(cmd, shell=True)






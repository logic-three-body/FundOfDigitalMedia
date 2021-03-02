#练习 1. 从本地读取一段视频，并获取帧数，帧率以及时长
import cv2
capture=cv2.VideoCapture('dog.mp4')
nbFrames = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
#获取其他一些视频帧相关参数
#CV_CAP_PROP_FRAME_WIDTH Width of the frames in the video stream #CV_CAP_PROP_FRAME_HEIGHT Height of the frames in the video stream
fps = int(capture.get(cv2.CAP_PROP_FPS))

wait = int(1/fps * 1000/1)
duration = (nbFrames * fps) / 1000
print('Num. Frames = ', nbFrames)
print('Frame Rate = ', fps, 'fps')
print('Duration = ', duration, 'sec')
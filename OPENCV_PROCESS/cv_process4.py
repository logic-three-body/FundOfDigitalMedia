#使用OpenCV可以从一个文件读取视频帧，并将其转换成NumPy数组。
#练习 4. 将视频读取到NumPy 数组中
import numpy as np
import cv2

cap = cv2.VideoCapture("dog.mp4")
wid = int(cap.get(3))
hei = int(cap.get(4))
framerate = int(cap.get(5))
framenum = int(cap.get(7))

video = np.zeros((framenum, hei, wid, 3), dtype='float16')

cnt = 0
while (cap.isOpened()):
    a, b = cap.read()
    cv2.imshow('%d' % cnt, b)
    cv2.waitKey(20)
    b = b.astype('float16') / 255
    video[cnt] = b
   #print(cnt) #143
    cnt+=1

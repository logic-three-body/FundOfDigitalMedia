#练习 2. 从摄像头读取视频并保存其中某一帧
import cv2
print(cv2.__file__)
cap = cv2.VideoCapture(0)#注意如果为1imshow会崩溃
while True:
    ret, im = cap.read()
    cv2.imshow('video test', im)
    key = cv2.waitKey(10)
    if key == 27:
        break
    if key == ord(' '):
        cv2.imwrite('vid_result.jpg',im)
cap.release()
cv2.destroyAllWindows()

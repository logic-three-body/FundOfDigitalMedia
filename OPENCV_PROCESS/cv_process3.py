#练习 3. 在 opencv窗口实时显示高斯模糊后的（彩色）图像
import cv2
print(cv2.__file__)
cap = cv2.VideoCapture(0)#注意如果为1imshow会崩溃
while True:
    ret, im = cap.read()
    blur = cv2.GaussianBlur(im, (0, 0), 5)
    cv2.imshow('video test', blur)
    key = cv2.waitKey(10)
    if key == 27:
        break
    if key == ord(' '):
        cv2.imwrite('vid_blur_result.jpg',blur)
cap.release()
cv2.destroyAllWindows()

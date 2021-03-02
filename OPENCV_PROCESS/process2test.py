import cv2
print(cv2.__file__)
impath='D:\Anaconda3\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml'
cap = cv2.CascadeClassifier(impath)
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

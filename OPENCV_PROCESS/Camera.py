import cv2

cam = cv2.VideoCapture(0)

wid = int(cam.get(3))
hei = int(cam.get(4))
size = (wid, hei)
fps = 30

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
out = cv2.VideoWriter()
out.open(r"C:\Users\75158\Desktop\OPENCV study\Yarn\video\AA.mp4",
         fourcc, fps, size)

while True:
    ret, frame = cam.read()
    if ret == False:
        break
    frame = cv2.flip(frame, 1)

    out.write(frame)
    cv2.imshow("frame", frame)

    key = cv2.waitKey(100)
    if cv2.waitKey(25) & 0xFF == ord('1'):  # 当按键 1 呗按下
        break
cam.release()
out.release()
cv2.destroyAllWindows()

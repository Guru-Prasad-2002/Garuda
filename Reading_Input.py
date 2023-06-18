import cv2

video=cv2.VideoCapture(1)

while True:
    success,img=video.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
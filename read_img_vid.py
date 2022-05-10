# Read images and videos
import cv2

# cap = cv2.VideoCapture("Resources/test_video.mp4") # download video on PC
cap = cv2.VideoCapture(0)  # inbuilt webcam
cap.set(3, 640)
cap.set(4, 480)

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

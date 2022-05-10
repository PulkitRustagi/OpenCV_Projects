# draw shapes and text
import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
# print(img.shape)
# img[:] = 0,200,255

cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 200, 255), 2)  # LINE format is (width, height)
cv2.rectangle(img, (0, 0), (200, 300), (250, 0, 255), cv2.FILLED)
cv2.circle(img, (400, 200), 50, (0, 255, 0), cv2.FILLED)
cv2.putText(img, "  Hello!  ", (150, 500), cv2.FONT_HERSHEY_SIMPLEX, 1, (150, 0, 255), 2)
cv2.imshow("Image", img)

cv2.waitKey(5000)

# Grayscale, Blur, Canny Edge detection, Dialation, Erosion
import cv2
import numpy as np

img = cv2.imread("Resources/lena.png")
kernel = np.ones((5, 5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # converts image to different color spaces
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)  # Blurs the image with (7,7) kernel size
imgCanny = cv2.Canny(img, 150, 200)
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)  # to increases thickness of detected edges
imgEroded = cv2.erode(imgDilation, kernel, iterations=1)  # to decrease thickness of detected edges

# cv2.imshow("Gray Image",imgGray)
# cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dilation Image", imgDilation)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(7000)

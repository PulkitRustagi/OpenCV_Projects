# detecting shapes by analysing contours, bounding boxes, after converting to GrayScale
import cv2
import numpy as np


def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL,
                                           cv2.CHAIN_APPROX_NONE)  # retrieves extreme outer contours
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area > 500:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            print(peri)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            print(len(approx))
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)
            if objCor == 3:
                objectType = "Tri"
            elif objCor == 4:
                aspRatio = w / float(h)
                if aspRatio > 0.95 and aspRatio < 1.05:
                    objectType = "Square"
                else:
                    objectType = "Rectange"
            elif objCor > 4:
                objectType = "Circel"
            else:
                objectType = "None"
            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 0, 255), 4)
            cv2.putText(imgContour, objectType, (x + (w // 2) - 10, y + (h // 2) - 10), cv2.FONT_HERSHEY_COMPLEX, 0.5,
                        (0, 0, 0), 2)


img = cv2.imread("Resources/shapes.png")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv2.Canny(imgBlur, 50, 50)
imgContour = img.copy()

getContours(imgCanny)
# cv2.imshow("Original",img)
# cv2.imshow("Image Gray",imgGray)
# cv2.imshow("Image Blur",imgBlur)
cv2.imshow("Image Canny Edge", imgCanny)
cv2.imshow("Image Contour", imgContour)

cv2.waitKey(10000)

# Warp an image of a card to straighten it in the output
import cv2
import numpy as np

img = cv2.imread("Resources/cards.png")

width, height = 250, 350
pts1 = np.float32([[111, 227], [300, 195], [157, 503], [366, 459]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Input Image", img)
cv2.imshow("Image Output Warped", imgOutput)

cv2.waitKey(4000)

# Resize and Crop images
import cv2

img = cv2.imread("Resources/lambo.png")
print(img.shape)
imgResized = cv2.resize(img, (350, 200))  # Resizing an image (width , height)
print(imgResized.shape)

imgCropped = img[0:200, 200:500]  # (height, width)

cv2.imshow("Input Image", img)
# cv2.imshow("Resized Image",imgResized)
cv2.imshow("Cropped Image", imgCropped)
cv2.waitKey(7000)

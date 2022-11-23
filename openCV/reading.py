import cv2 as cv
img = cv.imread("./abo.jpg")
cv.imshow('Abo',img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('img_hsv',img_hsv)


# capture = cv.VideoCapture(0)
# simple threshold
threshold, thresh= cv.threshold(gray,150,255,cv.THRESH_BINARY)
cv.imshow("simplethreshold", thresh)
threshold, thresh_inv= cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow("simplethresholdinv", thresh_inv) 
lower = 150
upper = 254
bright = cv.inRange(gray, lower, upper)

cv.imshow("bright", bright)
cv.waitKey(0)

'''
0-BLACK
255-pure white
'''
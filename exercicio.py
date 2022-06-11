import cv2 as cv
import numpy as np

base = cv.imread('./imagem/base.png')

median = cv.medianBlur(base, 9)


hsv_median = cv.cvtColor(median, cv.COLOR_BGR2HSV)
lowRedFilter = cv.inRange(hsv_median, (0, 0, 10), (15, 255, 200))
highRedFilter = cv.inRange(hsv_median, (160, 190, 50), (179, 255, 255))
redSelect = cv.add(lowRedFilter, highRedFilter)

result = cv.bitwise_and(base, base, mask=redSelect)

cv.imwrite('./imagem/result.jpg', result)
cv.imshow('result', result)
cv.waitKey(0)
cv.destroyAllWindows()
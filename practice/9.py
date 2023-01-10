# import cv2
# import numpy as np
# from matplotlib import pyplot as plt

# img = cv2.imread('data/lena.jpg')
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# kernal = np.ones((5,5), np.uint8)

# blur = cv2.blur(img, (5,5))
# canny = cv2.Canny(img, 100, 200)
# dilation = cv2.dilate(canny, kernal, iteration = 1)
# eroded = cv2.erode(dilation, kernal, iterations=1)

# cv2.imshow('blur', blur)
# cv2.imshow('Canny', canny)
# cv2.imshow('Dilation', dilation)
# cv2.imshow('Erode', eroded)

# cv2.waitKey()
# cv2.destroyAllWindows()
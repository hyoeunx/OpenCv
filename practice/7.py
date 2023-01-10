import cv2
import numpy as np
img = np.zeros((250,500,3), np.uint8)
img = cv2.rectangle(img, (200, 0), (300, 100), (255, 255, 255), -1)
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
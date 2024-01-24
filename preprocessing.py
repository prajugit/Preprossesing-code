import cv2
import matplotlib.pyplot as plt
import numpy as np

def preprocess(img):
    img = cv2.imread(rf'{img}')
    img = cv2.resize(img, (512,512))
    kernel = np.array([[0, -1, 0],
                    [-1, 5.3, -1],
                    [0, -1, 0]])
    img_sharpened = cv2.filter2D(img,-1,kernel)
    kernel_db = np.array([[1, 2, 1],
                   [2, 4, 2],
                   [1, 2, 1]]) / 16.0

    deblurred_img = cv2.filter2D(img_sharpened, -1, kernel_db)


    return deblurred_img
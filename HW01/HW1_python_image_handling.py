# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 00:36:30 2020

@author: jpan2
"""

import cv2
from matplotlib import pyplot as plt

img = cv2.imread('IMG_1584.jpg',-1)
plt.imshow(img)
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
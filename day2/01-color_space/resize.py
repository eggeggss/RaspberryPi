#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2017, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# resize.py
#
# Author : sosorry
# Date   : 2017/07/27
# Usage  : python resize.py

import cv2
import numpy as np

img = cv2.imread("lena256rgb.jpg")
rows, cols = img.shape[:2]

resize = cv2.resize(img, (2*rows, 2*cols), interpolation = cv2.INTER_CUBIC)
cv2.imshow('Resize', resize)
cv2.waitKey(0)

cv2.destroyAllWindows()


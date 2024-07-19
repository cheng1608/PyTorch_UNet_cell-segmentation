'cv2'
import cv2
import os
import glob

path = r'D:\py_project\SS1\group_50\mask\*.png'
for i in glob.glob(path):
    im1 = cv2.imread(i)
    im2 = cv2.resize(im1, (256, 256))
    cv2.imwrite(os.path.join(r'D:\py_project\SS1\teme\2', os.path.basename(i)), im2)
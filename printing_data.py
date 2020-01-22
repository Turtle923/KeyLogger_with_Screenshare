import numpy as np
import cv2
import time
import sys



lines = np.load("2020-01-19__28.361.npy",allow_pickle=True)

for data in lines:

	cv2.putText(data[0], "Keypressed : "+str(data[1]), (0, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)
	cv2.imshow('screen',data[0])
	cv2.waitKey(1000)
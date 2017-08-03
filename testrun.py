import numpy as np
from PIL import ImageGrab
import cv2
import time
import pyautogui
from pyautogui import dragTo as dragTo
from scanComet import scanforComet
from movingAround import patternedMovements
import pygame

# def process_img(image):
#     original_image = image
#     # convert to gray
#     processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     # edge detection
#     processed_img =  cv2.Canny(processed_img, threshold1 = 200, threshold2=300)
#     return processed_img

def main():
	while True:
		time.sleep(3)
		pyautogui.click(372,613)
		pyautogui.moveTo(372, 674)
		time.sleep(1)
		global config
		config='right'
		# pygame.init()
		while True:
			x,y=pyautogui.position()
			# x=patternedMovements(x)
			screen=np.array(ImageGrab.grab(bbox=(250,160,700,900)))
			screen, returnValue=scanforComet(screen, x)
			if returnValue==False:
				break

			# cv2.imshow('window',screen)
			# if cv2.waitKey(25) & 0xFF == ord('q'):
			# 	cv2.destroyAllWindows()
			# 	break

				
		pyautogui.click(286, 697)

if __name__ == "__main__":
	main()

#screen =  np.array(ImageGrab.grab(bbox=(250,160,700,900)))
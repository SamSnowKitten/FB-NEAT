import numpy as np
from PIL import ImageGrab
import cv2
import time
import pyautogui
from pyautogui import dragTo as dragTo

class movingDir():

	def __init__(self):
		self.direction='right'

	def move(self):
		x,y=pyautogui.position()

		if x>=480:
			self.direction='left'
		elif x<=250:
			self.direction='right'
		else:
			pass

		if self.direction=='left':
			pyautogui.dragRel(-33,0)
		elif self.direction=='right':
			pyautogui.dragRel(33,0)
		else:
			pass
		print(self.direction)

def scanforComet(screen):
	currentx,currenty=pyautogui.position()

	'''Creating an instance of the moving class'''
	moveChar=movingDir()

	'''Scans for Comet'''
	img_rgb = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
	img_gray= cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

	template=cv2.imread('comet.png',0)
	w, h= template.shape[::-1]
	res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
	threshold=0.9
	loc=np.where(res>=threshold)
	y, x=loc
	print(pyautogui.position())
	if x.size!=0:
		print(x+190)
		if (currentx>=(min(x)+140))&(currentx<=(max(x)+240)):
			moveChar.move()
	for pt in zip(*loc[::-1]):
		cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

	'''Checks for the end of the game'''
	pp_template=cv2.imread('character.png',0)
	w, h= pp_template.shape[::-1]
	res2 = cv2.matchTemplate(img_gray,pp_template,cv2.TM_CCOEFF_NORMED)
	threshold2=0.9
	loc2=np.where(res2>=threshold2)
	y2, x2=loc2
	if x2.size!=0:
		returnValue=False
	else:
		returnValue=True

	return img_rgb, returnValue

def main():
	while True:
		time.sleep(2)
		pyautogui.click(372,613)
		pyautogui.moveTo(372, 674)
		time.sleep(1)

		while True:
			x,y=pyautogui.position()
			screen=np.array(ImageGrab.grab(bbox=(250,160,700,900)))
			screen, returnValue=scanforComet(screen)
			if returnValue==False:
				break

		pyautogui.click(286, 697)

if __name__ == "__main__":
	main()
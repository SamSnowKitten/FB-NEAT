import numpy as np
import cv2
import pyautogui
from matplotlib import pyplot as plt
from movingAround import patternedMovements

def scanforComet(screen, currentx):
	# screen.astype(np.float32)
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
			config=patternedMovements(config='right')
	
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

	for pt in zip(*loc[::-1]):
		cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
	for pt in zip(*loc2[::-1]):
		cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

	# cv2.imshow('wefwe', img_rgb)
	# cv2.waitKey(0)
	return img_rgb, returnValue
# scanforComet(cv2.imread('test.png'))
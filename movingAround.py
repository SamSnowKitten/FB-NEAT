import cv2
import time
import pyautogui
from pyautogui import dragTo as dragTo 
def patternedMovements(config='right'):
   if (((round(100*time.time()))%2)==0):#&(x!=(round(time.time()))):
      x,y=pyautogui.position()
     
      if x>=350:
         pyautogui.dragTo(210, 675)
      pyautogui.dragRel(33,0)

      if x>=480:
         config='left'
      elif x<=250:
         config='right'
      else:
         pass
      
      if config=='left':
         pyautogui.dragRel(-33,0)
      elif config=='right':
         pyautogui.dragRel(33,0)
      else:
         print(config)
      print(config)
      return config







      # pyautogui.dragRel(33,0)
         # print(cposition, " ", round(time.time()))
         
          # if cposition==0:
          #    dragTo(365, 675)
          #    x=round(time.time())
          #    cposition+=1
          #    time.sleep(1)
          # elif cposition==1:
          #    dragTo(543, 675)
          #    x=round(time.time())
          #    cposition+=1
          #    time.sleep(1)
          # elif cposition==2:
          #    dragTo(210, 675)
          #    x=round(time.time())
          #    cposition-=2
          #    time.sleep(1)
          # else:
          #    print("error")
         # print(cposition, " ", round(time.time()))
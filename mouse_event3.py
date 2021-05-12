import numpy as np
import cv2

#events=[i for i in dir(cv2) if 'EVENT' in i ]
#print(events) 
#to get to know how many events are available 
#the following events are available :-- ['EVENT_FLAG_ALTKEY', 'EVENT_FLAG_CTRLKEY', 'EVENT_FLAG_LBUTTON', 'EVENT_FLAG_MBUTTON', 'EVENT_FLAG_RBUTTON', 'EVENT_FLAG_SHIFTKEY', 'EVENT_LBUTTONDBLCLK', 'EVENT_LBUTTONDOWN', 'EVENT_LBUTTONUP', 'EVENT_MBUTTONDBLCLK', 'EVENT_MBUTTONDOWN', 'EVENT_MBUTTONUP', 'EVENT_MOUSEHWHEEL', 'EVENT_MOUSEMOVE', 'EVENT_MOUSEWHEEL', 'EVENT_RBUTTONDBLCLK', 'EVENT_RBUTTONDOWN', 'EVENT_RBUTTONUP']

def click_event(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        blue=img[x,y,0]
        green=img[x,y,1]
        red=img[x,y,2]
        cv2.circle(img,(x,y),3,(0,0,255),-1)
        myimg=np.zeros((512,512,3),np.uint8)

        myimg[:]=[blue,green,red] #we want to fill every channel in the list , then we will pass the cannel values we got from BGR

        cv2.imshow('color',myimg)


#img=np.zeros((512,512,3),np.uint8)
img=cv2.imread('deer.jpg')
cv2.imshow('image',img)
points=[]
cv2.setMouseCallback('image',click_event) #2nd is the call back fucntion event 

cv2.waitKey(0)
cv2.destroyAllWindows()

#in this code if we click on a coloured img then in a new window the clicked colour will pop up
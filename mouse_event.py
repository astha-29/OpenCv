import numpy as np
import cv2

#events=[i for i in dir(cv2) if 'EVENT' in i ]
#print(events) 
#to get to know how many events are available 
#the following events are available :-- ['EVENT_FLAG_ALTKEY', 'EVENT_FLAG_CTRLKEY', 'EVENT_FLAG_LBUTTON', 'EVENT_FLAG_MBUTTON', 'EVENT_FLAG_RBUTTON', 'EVENT_FLAG_SHIFTKEY', 'EVENT_LBUTTONDBLCLK', 'EVENT_LBUTTONDOWN', 'EVENT_LBUTTONUP', 'EVENT_MBUTTONDBLCLK', 'EVENT_MBUTTONDOWN', 'EVENT_MBUTTONUP', 'EVENT_MOUSEHWHEEL', 'EVENT_MOUSEMOVE', 'EVENT_MOUSEWHEEL', 'EVENT_RBUTTONDBLCLK', 'EVENT_RBUTTONDOWN', 'EVENT_RBUTTONUP']

def click_event(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        print(x ,', ',y)
        font=cv2.FONT_HERSHEY_SIMPLEX
        strXY= str(x) + ',' + str(y)
        cv2.putText(img, strXY, (x,y),font,.5,(255,0,255),2)
        cv2.imshow('image',img)
    
    if event==cv2.EVENT_RBUTTONDOWN:
        blue=img[y,x,0] #it will start from 0 as in BGR blue has 0 index value
        green=img[y,x,1]
        red=img[y,x,2]
        font=cv2.FONT_HERSHEY_SIMPLEX
        strBGR= str(blue) + ',' + str(green)+ ' ,' +str(red)
        cv2.putText(img, strBGR, (x,y),font,.5,(0,0,255),2)
        cv2.imshow('image',img)


img=cv2.imread('deer.jpg')
cv2.imshow('image',img)

cv2.setMouseCallback('image',click_event) #2nd is the call back fucntion event 

cv2.waitKey(0)
cv2.destroyAllWindows()

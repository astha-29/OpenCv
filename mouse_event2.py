import numpy as np
import cv2

#events=[i for i in dir(cv2) if 'EVENT' in i ]
#print(events) 
#to get to know how many events are available 
#the following events are available :-- ['EVENT_FLAG_ALTKEY', 'EVENT_FLAG_CTRLKEY', 'EVENT_FLAG_LBUTTON', 'EVENT_FLAG_MBUTTON', 'EVENT_FLAG_RBUTTON', 'EVENT_FLAG_SHIFTKEY', 'EVENT_LBUTTONDBLCLK', 'EVENT_LBUTTONDOWN', 'EVENT_LBUTTONUP', 'EVENT_MBUTTONDBLCLK', 'EVENT_MBUTTONDOWN', 'EVENT_MBUTTONUP', 'EVENT_MOUSEHWHEEL', 'EVENT_MOUSEMOVE', 'EVENT_MOUSEWHEEL', 'EVENT_RBUTTONDBLCLK', 'EVENT_RBUTTONDOWN', 'EVENT_RBUTTONUP']

def click_event(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),4,(0,0,255),-1)
        points.append((x,y)) #we are saving the points whenever the mouse is clicked in thw form of array 
        if len(points)>=2:
            cv2.line(img,points[-1],points[-2],(255,0,0),5) #here -1 and -2 are the last and second last element of the array
            #if there are more than 2 points then the two points will be connected through a line.
        cv2.imshow('image',img)


img=np.zeros((512,512,3),np.uint8)
#img=cv2.imread('deer.jpg')
cv2.imshow('image',img)
points=[]
cv2.setMouseCallback('image',click_event) #2nd is the call back fucntion event 

cv2.waitKey(0)
cv2.destroyAllWindows()

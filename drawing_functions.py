import cv2
import numpy as np

#img=cv2.imread('deer.jpg', 1)
img=np.zeros([512,512,3],np.uint8) #it will give the black image

img=cv2.line(img, (0,0),(255,255), (255,0,0),5)
img=cv2.arrowedLine(img, (0,255),(255,255), (255,0,0),5)
img=cv2.rectangle(img,(384,0), (510,128),(0,255,0),-1)
img=cv2.circle(img, (447,63),63, (0,0,255),-1) #-1 REPRESENT THE FOLOUR FILLED 
font=cv2.FONT_HERSHEY_SIMPLEX
img =cv2.putText(img,'Opencv',(10,500),font,4,(255,255,255),10,cv2.LINE_AA) #HERE THE VALUE 10 IS THE THICKNESS 
cv2.imshow('image',img)

k=cv2.waitKey(0)

cv2.destroyAllWindows()

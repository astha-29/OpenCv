import cv2
img=cv2.imread('messi5.jpg')
img2=cv2.imread('logo.jpg')

print(img.shape) #returns a tuple of number of rows,columns and channels
print(img.size) #returns total number of pixels is accessed 
print(img.dtype) # returns image datatype is obtained 

b,g,r =cv2.split(img) #splitting the channel into 3
img=cv2.merge((b,g,r))

ball=img[280:340,330:390]
img[273:333, 100:160]=ball

img=cv2.resize(img,(512,512))  
img2=cv2.resize(img2,(512,512))
#add operation is only applicapble if the two images are of same size 
#dst=cv2.add(img,img2); 
#for normal adding

#for giving weight while adding
dst=cv2.addWeighted(img,.5, img2,.5,0); #here 0 is the gamma value 

cv2.imshow('image',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

#ROI- region of intrest 
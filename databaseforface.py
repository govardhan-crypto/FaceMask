import cv2
import os
dataset = "dataset"
name = "with_mask"

path = os.path.join(dataset,name)
if not os.path.isdir(path):
    os.mkdir(path)
(width,height)= (130,100)

alg ="haarcascade_frontalface_default.xml"

haar_cascade = cv2.CascadeClassifier(alg)

cam = cv2.VideoCapture(0)
count=1

#import urllib.request
#import cv2
#import numpy as np
#import imutils

#url = 'http://192.168.0.158:8080/shot.jpg'
while count < 101:
    print(count)
    #imgPath = urllib.request.urlopen(url)
    #imgNp = np.array(bytearray(imgPath.read()),dtype=np.uint8)
    #img = cv2.imdecode(imgNp,-1)
    #img = imutils.resize(img,width=450)

    _,img = cam.read()
    grayImg  = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face = haar_cascade.detectMultiScale(grayImg,1.3,4)
    for (x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        faceonly = grayImg[y:y+h,x:x+w]
        resizeImg = cv2.resize(faceonly,(width,height))
        cv2.imwrite("%s/%s.jpg"%(path,count),resizeImg)
        count+=1
    cv2.imshow("Facedetection",img)
    key = cv2.waitKey(10)
    if key == 27:
        break
print("image captured successfully ")    
cam.release()
    
 

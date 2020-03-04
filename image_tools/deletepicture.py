import cv2
import os
jpgpath='/home/ykang/10.12/image/'
jpgnames=os.listdir(jpgpath)
for i in jpgnames:
  #k=int(jpgnames[i][0:-4])
  #print(i[0:-4])
  k=int(i[0:-4])
  if(k%9==0):
     os.remove(jpgpath+i)

 

 

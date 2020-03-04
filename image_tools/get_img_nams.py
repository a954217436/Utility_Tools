import os
import numpy
imgpath='/home/ykang/opencv_yolov3/test/19'
imgnames=os.listdir(imgpath)
f=open('/home/ykang/opencv_yolov3/img_names.txt','w+')
for name in imgnames:
	name1=name+'\n'
	f.write(name1)

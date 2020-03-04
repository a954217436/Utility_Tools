import csv
import os
import cv2 as cv
import cv2

 
xml_path=('/home/ykang/darknet/VOCdevkit-25/VOC2007/Annotations/')
names=os.listdir(xml_path) 
for name in names:
	if 'enforce' in name:
		delpath=xml_path+name
		print(delpath)
		os.remove(delpath)
	
 
	



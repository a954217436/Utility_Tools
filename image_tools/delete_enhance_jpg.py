import csv
import os
import cv2 as cv
import cv2

img_path=('/home/ykang/darknet/VOCdevkit-25/VOC2007/JPEGImages/')
xml_path=('/home/ykang/darknet/VOCdevkit-25/VOC2007/target_data/yw_xml/')


names=os.listdir(img_path) 

for name in names:
	if 'enforce' in name:
		delpath=img_path+name
		print(delpath)
		os.remove(delpath)
	

	



# -*- coding:utf-8 -*-
import xml.etree.ElementTree as ET
import os
import shutil
import cv2 as cv

#从图片名中寻找目标图片

jpgpath='/home/ykang/darknet/VOCdevkit-25/VOC2007/JPEGImages/'
savepath='/home/ykang/darknet/VOCdevkit-25/VOC2007/target_data/sly_jpg/'
 

totaljpgs=os.listdir(jpgpath)

for jpgs in totaljpgs:
	if 'sly' in jpgs:
		imgpath=jpgpath+jpgs
		print(imgpath)
		img=cv.imread(jpgpath+jpgs)
		cv.imwrite(savepath+jpgs,img)



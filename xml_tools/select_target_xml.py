# -*- coding:utf-8 -*-
import xml.etree.ElementTree as ET
import shutil
import os
import shutil
import cv2 as cv

xmlpath='/home/ykang/darknet/VOCdevkit-25/VOC2007/Annotations/'
savexml='/home/ykang/darknet/VOCdevkit-25/VOC2007/target_data/hz_xml/'


totalxmls=os.listdir(xmlpath)


for xmls in totalxmls:
	if 'hzyw' in xmls:
		xml=xmlpath+xmls
		shutil.copy(xml,savexml)

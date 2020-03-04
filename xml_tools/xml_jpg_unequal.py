# -*- coding:utf-8 -*-
import xml.etree.ElementTree as ET
import os
import shutil
import cv2 as cv

jpgpath='/home/ykang/ycxw/JPEGImages/'
xmlpath='/home/ykang/ycxw/Annotations/'

jpgsname=os.listdir(jpgpath)
xmlsname=os.listdir(xmlpath)

#print(txtlines)

for xmlname in xmlsname:
    xmlname1=xmlname[:-4]
    xmlname2=xmlname1+'.jpg'
    if xmlname2 not in jpgsname:
       print(xmlpath+xmlname)
       os.remove(xmlpath+xmlname)
	 



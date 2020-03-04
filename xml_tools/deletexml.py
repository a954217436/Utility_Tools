# -*- coding:utf-8 -*-
import xml.etree.ElementTree as ET
import os
 
####删除与xml不对等的jpg图片

xml_path='/share/VOCdevkit/VOC2007/Annotations/'
jpg_path='/share/VOCdevkit/VOC2007/JPEGImages'
xml_names=os.listdir(xml_path)
jpg_names=os.listdir(jpg_path)
for name in xml_names:
     if not name in jpg_names:
        os.remove(xml_path+name)
           

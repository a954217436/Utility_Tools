# -*- coding:utf-8 -*-
import xml.etree.ElementTree as ET
import os
import shutil
xml_path='/home/dell/data/BZYB_selected_25/xml'
jpg_path='/home/dell/data/BZYB_selected_25/jpg'
xml_path_test='/home/dell/data/BZYB_selected_25/test/xml'
jpg_path_test='/home/dell/data/BZYB_selected_25/test/jpg'
f=open('/home/dell/data/BZYB_selected_25/test.txt')
for line in f:
        print(line[0:-1])
        xml_name=line[:-1]+'.xml'
        img_name=line[:-1]+'.jpg'
        shutil.move(os.path.join(xml_path,xml_name),os.path.join(xml_path_test,xml_name))
        shutil.move(os.path.join(jpg_path,img_name),os.path.join(jpg_path_test,img_name))
 

import sys
import os
import xml.etree.ElementTree as ET
import glob

xml_path = '/home/dell/BZYB_2/tyj/xml'
images_path = '/home/dell/BZYB_2/tyj/jpg'
xml_names=os.listdir(xml_path)
img_names=os.listdir(images_path)
k=0
n=0
for xml_name in xml_names:
    root = ET.parse(os.path.join(xml_path,xml_name)).getroot()
    filename = root.find('filename').text
    if filename[-4:]=='.JPG':
        #print(filename)
        n+=1
    img_name=xml_name[:-4]+'.jpg'
    if not os.path.exists(os.path.join(images_path,img_name)):
        os.remove(os.path.join(xml_path,xml_name))
for img_name in img_names:
    xml_name=img_name[:-4]+'.xml'
    if not os.path.exists(os.path.join(xml_path,xml_name)):#通过判断路径是否对应
        os.remove(os.path.join(images_path,img_name))
    if img_name[-4:]=='.jpg':
        #print(img_name)
        k=k+1
print(k)
print(n)
        

# -*- coding:utf-8 -*-
import xml.etree.ElementTree as ET
import os
prelabels=['bj_bpps','sly_bjbmyw','sly_dmyw','xmbhyc','yw_nc','yxcr','wcaqm','wcgz','hxq_gjbs','bj_bpmh']
xml_path='/share/VOCdevkit/VOC2007/Annotations'
xml_names=os.listdir(xml_path)
for name in xml_names:
    tree=ET.parse(os.path.join(xml_path,name))
    root=tree.getroot()
    objects=root.findall('object')
    #  此段代码判断label是否在xml文件里
    for object in objects:
        #print(object)
        label=object.find('name').text
        #print(label)
        if not label in prelabels:
            #print(1)
            root.remove(object)
    tree.write(os.path.join(xml_path,name))

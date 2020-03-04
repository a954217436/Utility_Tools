# -*- coding:utf-8 -*-
import os

#删除没有 特定  标签的数据

prelabels=['bmwh','yw_nc','hxq_gjbs']
xml_path='/home/ykang/DL/M2Det-master/VOCdevkit_test/VOC2007/Annotations'
jpg_path='/home/ykang/DL/M2Det-master/VOCdevkit_test/VOC2007/JPEGImages'
xml_names=os.listdir(jpg_path)
bmwh='bmwh'
yw_nc='yw_nc'
hxq_gjbs='hxq_gjbs'
for name in xml_names: 
    resa=bmwh  in name
    resb=yw_nc in name
    resc=hxq_gjbs in name
    resaa= bool(1-resa)
    resbb= bool(1-resb)
    rescc= bool(1-resc)
    if resaa&resbb&rescc:
          os.remove(os.path.join(jpg_path,name))

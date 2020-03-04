import os
import shutil
xml_path='/home/dell/data/BZYB_selected_25/xml_enforce'
xml_path_new='/home/dell/data/BZYB_selected_25/xml_all'
img_path='/home/dell/data/BZYB_selected_25/jpg_enforce'
img_path_new='/home/dell/data/BZYB_selected_25/jpg_all'
names=os.listdir(xml_path)
for name in names:
    xml_name=name
    img_name=name[:-4]+'.jpg'
    xml_path_new_all=os.path.join(xml_path_new,xml_name)
    img_path_new_all=os.path.join(img_path_new,img_name)
    if os.path.exists(xml_path_new_all):
        continue
    shutil.copy(os.path.join(xml_path,xml_name),xml_path_new_all)
    shutil.copy(os.path.join(img_path,img_name),img_path_new_all)




import sys
import os

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

path = 'Annotations_old/'

xml_list = os.listdir(path)

no_box_txt = open('no_box.txt', 'a')

for f in xml_list:
    tree = ET.parse(path + f)
    root = tree.getroot()
    obj = root.find('object')

    if obj is None:
        print('No object: ', f)
        no_box_txt.write(f.split('.')[0]+'\n')

    


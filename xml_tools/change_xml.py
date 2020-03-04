import os
import xml.dom.minidom
import xml.etree.ElementTree
 
xmldir = '/home/ykang/tf-api/VOCdevkit/VOC2007/Annotations/' 
xmlfiles=os.listdir(xmldir)
print(xmlfiles)
for xmlfile in os.listdir(xmldir):
    xmlname = os.path.splitext(xmlfile)[0]
    print(xmlname)
    #读取 xml 文件
    dom = xml.dom.minidom.parse(os.path.join(xmldir,xmlfile))
    root = dom.documentElement
 
    #获取标签对的名字，并为其赋一个新值
    root.getElementsByTagName('filename')[0].firstChild.data = xmlname + '.jpg'
    root.getElementsByTagName('path')[0].firstChild.data = \
    '/home/ykang/tf-api/VOCdevkit/VOC2007/JPEGImages/' + xmlname + '.jpg'

    #修改并保存文件
    xml_specific = xmldir + xmlfile 
    with open(xml_specific,'w') as fh:
        dom.writexml(fh)
 

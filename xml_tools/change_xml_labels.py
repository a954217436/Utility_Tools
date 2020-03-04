-import os
import xml.dom.minidom
import xml.etree.ElementTree as ET

xmldir = '/home/ykang/DATA/ycxw/Annotations/'
xmlfiles = os.listdir(xmldir)
# print(xmlfiles)
for xmlfile in xmlfiles:
    xmlname = os.path.splitext(xmlfile)[0]
    dom = xml.dom.minidom.parse(os.path.join(xmldir, xmlfile))
    root = dom.documentElement
    k=len(root.getElementsByTagName('name'))
    for i in range(0,k):
        if root.getElementsByTagName('name')[i].firstChild.data == 'hat':
            root.getElementsByTagName('name')[i].firstChild.data = 'aqmzc'
        else:
            root.getElementsByTagName('name')[i].firstChild.data = 'wcaqm'
    xml_specific = xmldir + xmlfile
    with open(xml_specific, 'w') as fh:
        dom.writexml(fh)


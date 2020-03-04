import cv2
import csv
import os
import shutil
from PIL import Image
import numpy

classes=['bjdsyc','gbps','ywzt_yfyc','sly_bjbmyw','wcaqm','mcqdmsh','hxq_gjbs','hxq_gjtps','yw_nc','jyz_lw','sly_dmyw','bj_wkps','jsxs','yw_gkxfw',
'wcgz','gjptwss','xmbhyc','bj_bpmh','bj_bpps','ybf','yxcr','bmwh','xy','jyz_pl','ybh']
lines=[]
for i in range(len(classes)):
    f1=open('/home/ykang/darknet/results/dafen/result/yjh_'+classes[i]+'_result.csv')
    f11=csv.reader(f1)
    for line in f11:
        if line[0]=='filename':
            continue
        lines.append(line)



shutil.rmtree('/home/ykang/darknet/results/dec_img')
os.makedirs('/home/ykang/darknet/results/dec_img')
lines=sorted(lines,key=lambda x:x[0])
img_path='/home/ykang/darknet/VOCdevkit/VOC2007/JPEGImages'
img_name=lines[0][0]
 
image = Image.open(os.path.join(img_path,img_name))
img = cv2.cvtColor(numpy.asarray(image),cv2.COLOR_RGB2BGR)
#img=cv2.imread(os.path.join(img_path,img_name))
#print(lines)
for line in lines:
    print(line)
    img_name_temp=line[0]
    if img_name_temp==img_name:
        label=line[1]#put up the label
        score=line[2]
        xmin=int(float(line[3]))
        ymin=int(float(line[4]))
        xmax=int(float(line[5]))
        ymax=int(float(line[6]))
        cv2.rectangle(img,(xmin,ymin),(xmax,ymax),(0,255,0),8)
        font = cv2.FONT_HERSHEY_SIMPLEX
        text=str(label)
        cv2.putText(img, text, (xmin, ymin-50), font, 4, (0,0,255), 12)
    else:
        cv2.imwrite('/home/ykang/darknet/results/dec_img/'+img_name,img)
        img_name=img_name_temp
        image = Image.open(os.path.join(img_path,img_name))
        img = cv2.cvtColor(numpy.asarray(image),cv2.COLOR_RGB2BGR)
        #img=cv2.imread(os.path.join(img_path,img_name))
        label=line[1]#put up the label
        score=line[2]
        xmin=int(float(line[3]))
        ymin=int(float(line[4]))
        xmax=int(float(line[5]))
        ymax=int(float(line[6]))
        cv2.rectangle(img,(xmin,ymin),(xmax,ymax),(0,255,0),8)
        font = cv2.FONT_HERSHEY_SIMPLEX
        text=str(label)
        cv2.putText(img, text, (xmin, ymin-50), font, 4, (0,0,255), 12)


f=open('/home/ykang/darknet/VOCdevkit/VOC2007/ImageSets/Main/test.txt')
line_all=[]
for line in f:
    line_all.append(line)
line_ex=os.listdir('/home/ykang/darknet/results/dec_img/')
#print(line_ex)
for line in line_all:
    if line[:-1]+'.jpg' in line_ex:
        print(line)
        continue
    else:
        #print(line+'.jpg')
        img=cv2.imread(os.path.join(img_path,line+'.jpg'))
        cv2.imwrite('/home/ykang/darknet/results/dec_img/'+line+'.jpg',img)

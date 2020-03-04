import cv2
import os
img_path='/home/yjh/ObjectDetection-OneStageDet/yolo/VOCdevkit/VOC2007/JPEGImages'
f=open('/home/yjh/ObjectDetection-OneStageDet/yolo/VOCdevkit/VOC2007/ImageSets/Main/test.txt')
line_all=[]
for line in f:
    line_all.append(line)
line_ex=os.listdir('/home/yjh/ObjectDetection-OneStageDet/yolo/results/dec_img')
#print(line_ex)
for line in line_all:
    if line[:-1]+'.jpg' in line_ex:
        print(line)
        continue
    else:
        #print(line+'.jpg')
        img=cv2.imread(os.path.join(img_path,line+'.jpg'))
        cv2.imwrite('/home/yjh/ObjectDetection-OneStageDet/yolo/results/dec_img/'+line+'.jpg',img)

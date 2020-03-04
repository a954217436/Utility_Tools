import os
import random

jpgpath='./JPEGImages/'
ftrain = open('./ImageSets/Main/train.txt', 'r')  
ftest_new = open('./ImageSets/Main/test.txt', 'r')  
ftrain_new=open('./ImageSets/Main/train_new.txt', 'a+')
lines1=ftrain.readlines()
lines2=ftest_new.readlines()

jpgs=os.listdir(jpgpath)
#print(jpgs)
for name in lines1:
    name1=name[:-1]+'.jpg'
    if not name1 in jpgs:
        prnt(name)
        lines1.remove(name) 

for xml in lines1:
    ftrain_new.write(xml)
import cv2
vc = cv2.VideoCapture('/home/ykang/10.12/192.168.0.11_01_20191012103756379.mp4') #读入视频文件
c=10056
rval=vc.isOpened()
timeF = 5  #视频帧计数间隔频率
while rval:   #循环读取视频帧
    c = c + 1
    rval, frame = vc.read()
    #if(c%timeF == 0): #每隔timeF帧进行存储操作
#        cv2.imwrite('smallVideo/smallVideo'+str(c) + '.jpg', frame) #存储为图像
    if rval:
	    #img为当前目录下新建的文件夹
        cv2.imwrite('image/'+str(c) + '.jpg', frame) #存储为图像
        cv2.waitKey(1)
    else:
        break
vc.release()
 
 
 

 

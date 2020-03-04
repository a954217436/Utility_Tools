# -*- coding: UTF-8 -*-
# 2019/11/25 by LiuMin
# 画yolov3的损失值和平均损失值
# 输入的log日志文件内容为两列以逗号隔开的数据，第一列是loss，第二例如是agvloss


import os
import matplotlib.pyplot as plt
import numpy as np
 
MainDir = '/home/lm/Project/darknet'  #darknet 的路径
TrainLogPath = os.path.join(MainDir, 'backup', 'TrainLog_2019-12-4-20-50.txt') # log日志的路径
Loss, AgvLoss = [], []
with open(TrainLogPath, 'r') as FId: # 打开log文档
	TxtLines = FId.readlines() # 使用readlines()函数读取所有行(直到结束符 EOF)并返回列表
	for TxtLine in TxtLines: # 依次读取TxtLines里的每行
		SplitStr = TxtLine.strip().split(',') # 根据逗号分割对字符串进行切片
		Loss.append(float(SplitStr[0])) # 第一列为当前迭代次数的损失值
		AgvLoss.append(float(SplitStr[1])) # 第二列为平均损失值
 
IterNum = len(AgvLoss) # 计算平均损失列表的长度
StartVal, EndVal, Stride = 10000, IterNum, 100 # 从迭代次1000次开始画图，因之前迭代的损失值较大，不利于分析，每隔50画一个点，可以视情况修改
Xs = np.arange(StartVal, EndVal, Stride) # 使用arange()创建等差数组，制作x轴
Ys = np.array(Loss[StartVal:EndVal:Stride]) # 跳着切片，y轴范围从1000到IterNum，每50画一个点
YAs = np.array(AgvLoss[StartVal:EndVal:Stride]) 
plt.plot(Xs, Ys,'r-',label='loss')
plt.plot(Xs, YAs,'b-',label='avg_loss')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Loss-Iter curve")
plt.legend() # plt.legend()主要的作用就是给图加上图例
plt.show()


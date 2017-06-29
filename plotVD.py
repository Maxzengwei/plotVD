import pandas as pd
import matplotlib.pyplot as plt
from math import *


def calSpeed(L1,L2):   #计算速度 分别为前后两帧图像
	speed=0
	count=0
	for i in L1:
		for ii in L2:
			print(i[0],ii[0])
			if i[0]==ii[0]:
				count=count+1
				speed=speed+sqrt((i[2]-ii[2])**2+(i[3]-ii[3])**2)
	print(speed)
	if count==0:
		return 0
	return speed/count
	

def select(L,store,sameL):  #选择出规定区域
	for i in store:
		if i[2]>=0 and i[2]<=100 and i[3]>=0 and i[3]<=100:
			L.append(i)
#			print(i)
	count=1
	for ii in range(totalFrames):
		sameL.append([])
		for i in L:
			if i[0]==count:
				sameL[ii].append(i)
		count=count+1
	return L,sameL


############################
#计算文件中单用户单帧速度
#当中帧根据当前帧前后两帧位移，计算速度；
#端点帧，根据最近帧位移，计算速度
def calSpeed2(store,index):
	if store[index][1] == 0:
		return (sqrt((store[index+1][2]-store[index][2])**2+(store[index+1][3]-store[index][3])**2))/(1/25)/100
	elif store[index][1]  == totalFrames:
		return (sqrt((store[index-1][2]-store[index][2])**2+(store[index-1][3]-store[index][3])**2))/(1/25)/100
	else:
		return (sqrt((store[index-1][2]-store[index+1][2])**2+(store[index-1][3]-store[index+1][3])**2))/(2/25)/100

def select2(L,store,sameL):  #选择出规定区域
	for index,i in enumerate(store):
		if i[2]>=0 and i[2]<=100 and i[3]>=0 and i[3]<=100:		
			i.append(calSpeed2(store,index))
			L.append(i)
#			print(i)
	for frameNum in range(totalFrames):
		sameL.append([])
		for i in L:
	 		if i[1]==frameNum:
	 			sameL[frameNum].append(i)
	return L,sameL



f=open('1_v2.txt')
store=[]
totalFrames = 0
for index,i in enumerate(f):
	#print(i)
	store.append(i.strip().split(' '))
	store[index][2]=float(store[index][2])
	store[index][3]=float(store[index][3])
	store[index][1]=int(store[index][1])
	store[index][0]=int(store[index][0])
	totalFrames=max(totalFrames,store[index][1])
# store=[]
def check(L):
	for i in L:
		print(i)

#main_procedure
L=[]
sameL=[]
L,sameL=select2(L,store,sameL)
check(sameL)

#print(len(sameL))
speed={} #速度和
desnity={} #人数和
for index,someL in enumerate(sameL):
#	print(index,len(someL),someL)
	count = len(someL)
	if(count>0):
		if count not in desnity.keys():
			desnity[count] = 0
		if count not in speed.keys():
			speed[count] = 0
		desnity[count]+=count
		for data in someL:
			print(data[5],speed[count])
			speed[count]+=data[5]

avgSpeed={}
for k in speed.keys():
	print(k,speed[k],desnity[k])
	avgSpeed[k]=speed[k]/desnity[k]
# #print(avgSpeed)
plt.scatter([float(k) for k in avgSpeed.keys()],[float(v) for v in avgSpeed.values()])
plt.show()
	
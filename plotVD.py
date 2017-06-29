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
	for ii in range(2957):
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
	previousFrame = store[index-1]
	nextFrame = store[index+1]
	if previousFrame[1]==previousFrame[1] :
		return (sqrt((previousFrame[2]-nextFrame[2])**2+(previousFrame[3]-nextFrame[3])**2))*2/25
	elif previousFrame[1]==store[index][1]:
		return (sqrt((previousFrame[2]-store[index])**2+(previousFrame[3]-store[index])**2))*1/25
	elif nextFrame[1]==store[index][1]:
		return (sqrt((nextFrame[2]-store[index])**2+(nextFrame[3]-store[index])**2))*1/25

def select2(L,store,sameL):  #选择出规定区域
	for index,i in enumerate(store):
		if i[2]>=0 and i[2]<=100 and i[3]>=0 and i[3]<=100:		
			i.append(calSpeed2(store,index))
			L.append(i)
#			print(i)
	for frameNum in range(2957):
		sameL.append([])
		for i in L:
	 		if i[1]==frameNum:
	 			sameL[frameNum].append(i)
	return L,sameL



f=open('1_v2.txt')
store=[]
for index,i in enumerate(f):
	#print(i)
	store.append(i.strip().split(' '))
	store[index][2]=float(store[index][2])
	store[index][3]=float(store[index][3])
	store[index][1]=int(store[index][1])
	store[index][0]=int(store[index][0])
# store=[]
def check(L):
	for i in L:
		print(i)

#main_procedure
L=[]
sameL=[]
L,sameL=select2(L,store,sameL)
#check(sameL)

#print(len(sameL))
speed={} #速度和
desnity={} #人数和
for index,someL in enumerate(sameL):
#	print(index,len(someL),someL)
	if len(someL) not in desnity.keys():
		desnity[len(someL)] = 0
	if len(someL) not in speed.keys():
		speed[len(someL)] = 0
	desnity[len(someL)]+=len(someL)
	for data in someL:
		speed[len(someL)]+=data[5]

avgSpeed={}
for k in speed.keys():
	avgSpeed[k]=speed[k]/desnity[k]
print(avgSpeed)
plt.scatter([float(k) for k in avgSpeed.keys()],[float(v) for v in avgSpeed.values()])
plt.show()
	# 	print(index,len(data),data)

# if index+25<len(sameL):
# 	desnity.append(len(i))
# 	speed.append(calSpeed(i,sameL[index+25]))
	
# print(len(desnity),len(speed))
# print(speed)
# plt.scatter(desnity,speed)
# plt.show()

# data = pd.read_table('1_v2.txt',header=None,delim_whitespace=True,index_col=0)
# sampledata = data[(data[2]>=0) & (data[2]<=100) & (data[3]>=0) & (data[3] <= 100)]

# framedata=[]
# for frameindex in range(2957):
# 	framedata.append([])
# 	framedata[frameindex] = sampledata[(sampledata[1] == frameindex)]
# print(framedata[2847])








#data.describe()
import pandas as pd
import matplotlib.pyplot as plt
from math import *



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

for index,i in enumerate(store):
	print(i[2],i[3])

plt.scatter([k[2] for index,k in enumerate(store)],[k[3] for index,k in enumerate(store)])
plt.show()
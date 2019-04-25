import matplotlib.pyplot as pt
import numpy as np
# import matplotlib
# print(matplotlib.__file__)

pt.rcParams['font.sans-serif']=['SimHei']
pt.rcParams['axes.unicode_minus']=False

with open('climate.txt','r',encoding='utf-8') as fp:
	climate = fp.readlines()

def show():
	for i in range( len(weather) ):
		# enter = 
		print( " {:>2} {:<3}".format(i,weather[i][0]) , end="   ")
		if (i+1) % 5 == 0:
			print()	

def ShowWeather(k):
	temperature = list()
	for i in range(1,13):
		temperature.append(float(weather[k][i]))
	ind = np.arange(12)
	pt.barh(ind, temperature)
	pt.yticks(ind, month)
	pt.title(weather[k][0])
	pt.show()

weather = []

for i in climate:
	block = i.rstrip('\n').split('\t')
	weather.append(block)
# show()
month = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOB','DEC']
while( True ):
	show()
	num = int(input("Enter the num you want to find(End in -1):"))
	if num == -1 :
		break
	ShowWeather(num)
	x = input("Enter enter to go back")
	print()
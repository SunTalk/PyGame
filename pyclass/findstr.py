D = {}

target = input("target=")
target = target.lower()

listS = list(target)
	
for i in range( 0,len(listS) ):
	tmp = listS[i]
	if tmp in D.keys():
		D[tmp] = D[tmp]+1
	else:
		D[tmp] = 1

for j in D:
	print( "{} : {}".format(j,D[j]) )
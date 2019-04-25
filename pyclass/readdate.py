p = open("bump.txt","r")
list_star = p.readlines()
f = open("output.out","w")

row = len(list_star)
column = len(list_star[0])

for j in range(0,column):
	for i in range(row-1,-1,-1):
		f.write(list_star[i][j])
	f.write("\n")
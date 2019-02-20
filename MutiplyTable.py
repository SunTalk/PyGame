
for i in range(1,10):
	for j in range(1,10):
		ans = i*j
		print(i,"*",j,"=",ans)
	print()
print("-----------------------------------------------------------------------------------------------------------")
print()
for i in range(1,10):
	for j in range(1,10):
		ans = str(i*j)
		if i*j < 10:
			ans = " " + ans
		print(i,"*",j,"=",ans,end="  ")
	print()
print()
print("-----------------------------------------------------------------------------------------------------------")
print()
for i in range(1,10,3):
	for j in range(1,10):
		for k in range(i,i+3):
			ans = str(k*j)
			if k*j < 10:
				ans = " "+ans
			print( k,"*",j,"=",ans,end = "  ")
		print()
	print()

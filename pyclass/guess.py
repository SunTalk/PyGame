import random

upper = 99
lower = 0
count = 0
ans = random.randint(0,99)

while 1 :
	print( "Guess in(",lower,"," ,upper,")" )
	test = int(input())
	count = count + 1

	if test < lower or test > upper:
		print( "Your guess is not in range" )
	elif test < ans :
		lower = test
	elif test > ans :
		upper = test;
	else :
		print("You are right")
		break

print("You guess",count,"times")

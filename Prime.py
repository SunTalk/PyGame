import math
def isPrime(k):
	for i in range(2,int(math.sqrt(k))+1):
		if k%i == 0:
			return 0
	return 1

List = [ ]

def prime_list(a,b):
	for j in range(a,b+1):
		if isPrime(j):
			List.append(j)

a = int(input("a="))
b = int(input("b="))
prime_list(a,b)

print("{} to {} has prime {} ".format(a,b,List ) )

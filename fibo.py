D = {0:0,1:1}
def fibo_recursive_DP(k):
	if k in D.keys():
		return D[k]
	else:
		tmp = fibo_recursive_DP(k-1) + fibo_recursive_DP(k-2)
		D[k] = tmp
	return tmp

def fibo_recursive(k):
	if k < 2:
		return k
	else:
		tmp = fibo_recursive(k-1) + fibo_recursive(k-2)
	return tmp

def fibo_for_loop(k):
	if k < 2:
		return k
	else:
		a = 0
		b = 1
		for i in range(1,k):
			tmp = a + b
			a = b
			b = tmp
	return tmp

num = int(input("num="))

print( fibo_recursive_DP(num) )
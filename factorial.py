n = int(input("Веди число: "))
def matrix(n):
	if n == 0:
		return 1
	return matrix(n-1) * n 
print(matrix(n))










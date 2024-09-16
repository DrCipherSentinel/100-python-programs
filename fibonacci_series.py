def main():
	n=int(input("enter a number:"))
	print("fibonacci series:",fibonacci(n))

def fibonacci(n):
	fibonacci_series=[]
	a,b=0,1
	if n<0:
		print("enter positive number")
	elif n==0:
		return a
	else:
		for i in range(n):
			fibonacci_series.append(a)
			a,b=b,b+1
		return fibonacci_series

if __name__=="__main__":
	main()

def main():
	num = int(input("enter a number: "))
	if num<0:
		print("entered a negative number")
	elif num==0:
		print("factorial of 0 is 1")
	else:
		res=factorial(num)
		print(f"The factorial of {num} is {res}")

def factorial(n):
	if n==0:
		return 1
	else:
		return n*factorial(n-1)

if __name__=="__main__":
	main()

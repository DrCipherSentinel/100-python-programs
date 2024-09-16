def armstrong(num):
	arm_str=str(num)
	a = len(arm_str)
	arm_sum=0
	for i in arm_str:
		arm_sum += int(i)**a
	return num == arm_sum
	
num = int(input("enter a number="))
if armstrong(num):
	print(f"{num} is a armstrong number")
else:
	print(f"{num} is not a armstrong number")

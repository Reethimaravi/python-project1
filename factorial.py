n = input("enter a number: ")
fact = 1
if n == 0:
	print("factorial of 0 is 0")
else:
	for i in range(1,n+1):
		fact = fact * i
	print("factorial : {0}".format(fact))
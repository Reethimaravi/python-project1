num = input("enter a number: ")
temp = num
sum = 0
while num > 0:
	r = num % 10
	sum  += r**3
	num //= 10
if(temp == sum):
	print("Amstrong Number....")
else:
	print("Not amstrong number")
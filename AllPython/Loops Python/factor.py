#P4.16 
inputnumber = int(input("what is the number you would like to factor")
i = 2
while i <= inputnumber:
	if inputnumber % i == 0:
	print(i)
	inputnumber /= i
else:
	i = i + 1

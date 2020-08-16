
def main():

	num1 = input("Enter the first number: ")
	try:
		num1 = int(num1)
	except ValueError:
		print("Not a valid number ")
	else:
		pass

	num2 = input("Enter the second number: ")
	try:
		num2 = int(num2)
	except ValueError:
		print("Not a valid number ")
	else:
		pass

	opr = input("Choose an operation from the following (+, -, /, *): ")


	if opr == "+" :
		result = int(num1) + int(num2)
	elif opr == "-":
		result = int(num1) - int(num2)
	elif opr == "/":
		result = int(num1) / int(num2)
	elif opr=="*":
		result = int(num1) * int(num2)
	else:
			print("The operation entered is not valid")


	print (result)




if __name__ == '__main__':
	main()

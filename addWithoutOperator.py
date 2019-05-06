def addWithoutOperator(x,y):
	while y!= 0:
		carry = x&y
		x=x^y
		y=carry<<1
	print('Answer is {}'.format(x))

def main():
	raw_input = input("Enter two numbers:")
	x,y = map(int,raw_input.split())
	addWithoutOperator(x,y)

main()	

#print(addWithoutOperator(2,3))
	

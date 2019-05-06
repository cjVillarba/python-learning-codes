def is_unique(str):
	str = str.replace(" ","").lower()
	check = {}
	for letter in str:
		if letter in check:
			check[letter]=1
		else:
			check[letter] =0
			
	print(check)
	
	for k in check:
		if check[k] == 0:
			return True
		else:
			return False

st = 'strin sg'
print(is_unique(st))
def is_permutation2(st1,st2):
	
	if len(st1) != len(st2):
		return False
		
	count = {}
	
	for char in st1:
		if char in count:
			count[char] += 1
		else:
			count[char] = 1
	
	for char in st2:
		if char in count:
			count[char] -= 1
		else:
			count[char] = 1
	
	for k in count:
		if count[k] != 0:
			return False
		count[k] = True
	
	return True
	
st1 = 'abcde'
st2 = 'dcbefa'

print(is_permutation2(st1,st2))
	
	
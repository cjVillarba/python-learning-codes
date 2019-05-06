def is_anagram2(st1,st2):
	
	st1 = st1.replace(" ","").lower()
	st2 = st2.replace(" ","").lower()

	count = {}
	
	for letter in st1:
		if letter in count:
			count[letter] += 1
		else:
			count[letter] = 1
			
	for letter in st2:
		if letter in count:
			count[letter] -= 1
		else:
			count[letter] = 1
			
	#print(count)		
	
	for k in count:
		if count[k] != 0:
			return False
		else:
			count[k] = True
			
	return True

st1 = 'ana gram'
st2 = 'grams ana'

print(is_anagram2(st1,st2))
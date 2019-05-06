#print(ord('h'))

def is_unique2(str):
	if len(str) > 128:
		return False
		
	char_set = [False for x in range(128)]
	
	for char in str:
		val = ord(char)
		if char_set[val]:
			return False
		char_set[val] = True
	
	return True

st1 = 'strinsg'

print(is_unique2(st1))
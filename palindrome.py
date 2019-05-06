def palindrome(str):
	
	l = len(str)
	
	count={}
	
	for i in range(l//2):
		if str[i] != str[-1-i]:
			return False
		else:
			count[i] = True
			
#	print(count)
		
	return True
			
s = 'cowoc'
#print(len(s))
print(palindrome(s))
def urlify2(str, length):
	
	str = list(str.strip())
	 #strip() is not in-place
	new_index = len(str)
	
	print(len(str))
	print(str)
	
	index = 0
	new_str=[]
	for i in range(length):
		if str[i] == ' ':
			new_str[index:index+3] = '%20'
			index += 3
		else:
			new_str[index] = str[i]
			index += 1
	
	print(new_str)
	return "".join(new_str)

str = 'Mr John Smith   '
#print(str.strip(' ').replace(' ','%20'))
print(urlify2(str,13))
#def select_int(s):
	
s = input()
l = len(s)
	
i = 0
while i<l:
	num = ''
	sym = s[i]
	
	while sym.isdigit():
		num += sym
		i += 1
		if i<l:
			sym = s[i]
		else:
			break	
		
	if num != '':
		print(num)
	i += 1
			
a = 'th 67 dhhd 78'
print(type(a))
#print(int(a))	#This is an error!
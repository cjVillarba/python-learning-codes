from random import random

def max_digit(num):
	
	str_num = str(num)
	
	max_num = -1
	
	for i in range(len(str_num)):
		if str_num[i] == '.':
			continue
		elif int(str_num[i]) > max_num:
			max_num = int(str_num[i])
	
	return max_num
	
#print(round(random()*1000,3))

n = round(random()*1000,3)
print(n)
#print(len(n))
print(max_digit(n))
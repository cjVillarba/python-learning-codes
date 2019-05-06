def is_anagram(st1,st2):
	st1 = st1.replace(" ","").lower()
	st2 = st2.replace(" ","").lower()
	
	return sorted(st1) == sorted(st2)
	
st1 ='civic'
st2 ='vicic'
print(is_anagram(st1,st2))
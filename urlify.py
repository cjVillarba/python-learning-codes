def urlify(st):
	return st.strip().replace(" ",'%20')
	
st = "Mr John Smith "

print(urlify(st))
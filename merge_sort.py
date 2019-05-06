def merge(left,right):
	result=[]
	n,m=0,0
	while n<len(left) and m<len(right):
		if left[n]<=right[m]:
			result.append(left[n])
			n += 1
		else:
			result.append(right[m])
			m += 1
			
	result += left[n:]
	result += right[m:]
	return result
	
def sort(seq):
	if len(seq)<=1:
		return seq
	mid = int(len(seq)/2)
	left = sort(seq[:mid])
	right = sort(seq[mid:])
	return merge(left,right)
	
seq = [2,1,4,3,5]
print(sort(seq))
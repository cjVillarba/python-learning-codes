def quick_sort(seq):
	if len(seq) <= 1:
		return seq
	else:
		pivot = seq[0]
		left,right =[],[]
		for x in seq[1:]:
			if x<pivot:
				left.append(x)
			else:
				right.append(x)
		return sorted(left) + [pivot] + sorted(right)
		
seq = [2,1,4,3,5]
s = quick_sort(seq)
print(s)

print([1,2,3]+[4]+[5,6,7])
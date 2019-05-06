def bubble_sort(seq):
	
	l = len(seq)
	for i in range(l):
		for j in range(1,l-i):
			if seq[j] < seq[j-1]:
				seq[j-1],seq[j] = seq[j],seq[j-1]
	return seq
	
seq =[2,5,1,3,7,6,8,9]
print(bubble_sort(seq))
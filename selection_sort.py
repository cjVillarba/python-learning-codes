def selection_sort(seq):
	for i in range(len(seq)):
		iMin = i
		for j in range(i+1,len(seq)):
			if seq[iMin] > seq[j]:
				iMin = j
		if i != iMin:
			seq[i], seq[iMin] = seq[iMin], seq[i]
	return seq
	
seq = [2,1,3,5,4]
s = selection_sort(seq)
print(s)
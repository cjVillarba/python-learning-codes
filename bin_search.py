def bin_search(seq,k):
	
	lo = 0
	hi = len(seq)-1
	
	while hi>=lo:
		
		mid = lo +(hi-lo)//2
		
		if seq[mid] < k:
			lo = mid +1
		elif seq[mid] > k:
			hi = mid-1
		else:
			return mid
					
	return 'Not Found'
		
		
seq = [1,2,3,5,6,8,9]
k = 7
print(bin_search(seq,k))
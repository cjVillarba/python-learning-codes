class MergeSort(object):
	def merge(self, left,right):
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
	
	def sort(self, seq):
		if len(seq)<=1:
			return seq
		mid = int(len(seq)/2)
		left = sorted(seq[:mid])
		right = sorted(seq[mid:])
		return self.merge(left,right)
	
seq = [2,1,56,4,3,5]
test = MergeSort()
print(test.sort(seq))

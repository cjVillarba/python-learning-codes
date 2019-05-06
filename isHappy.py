class Solution:
	
	def isHappy(self, n):
		lookup = {}
		while n != 1 and n not in lookup:
			lookup[n] = True
			n = self.nextNumber(n)
			print(lookup)
		return n == 1, lookup
	
	def nextNumber(self, n):
		new = 0
		for char in str(n):
			new += int(char)**2
		return new
		
x = Solution()
print(x.isHappy(19))
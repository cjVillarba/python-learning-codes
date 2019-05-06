class Solution(object):
	def reverse(self,x):
		if x<0:
			return -self.reverse(-x)
			
		result = 0
		while x:
			result = result *10+x%10
			x //=10
		return result if result <= 0x7fffffff else 0


num = Solution()
ans = num.reverse(123)
print(ans)
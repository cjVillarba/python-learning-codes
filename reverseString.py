class Solution(object):
	def reverseString(self,s):
		str = list(s)
		i, j = 0, len(str)-1
		while i<j:
			str[i], str[j] = str[j],str[i]
			i += 1
			j -= 1
		return "".join(str)
		
	def reverseString2(self,s):
		return s[::-1]
		
string = Solution()
ans=string.reverseString("Charlie The Great!")
print(ans)

ans=string.reverseString2("God is the Greatest!")
print(ans)
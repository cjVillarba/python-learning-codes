import operator
import collections
from functools import reduce

class Solution(object):
	def findTheDifference(self,s,t):
		return chr(reduce(operator.xor,map(ord,s),0)^reduce(operator.xor,map(ord,t),0))
		
	def findTheDifference2(self,s,t):
		s = list(s)
		t = list(t)
		for i in s:
			t.remove(i)
		return t[0]
	
	def findTheDifference3(self,s,t):
		s,t = sorted(s),sorted(t)
		return t[-1] if s == t[:-1] else [x[1] for x in zip(s,t) if x[0] != x[1]][0]
		
		
test = Solution()
s="abcd"
t="abcde"
#print(list(s))
ans = test.findTheDifference(s,t)
print(ans)

#print(map(ord,s))
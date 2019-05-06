#import operator
#print(dir(operator))

num = [3,20,34,5,9]
print(num)
y = [str(x) for x in num]
y.sort()
print(y,'\n\n')
print(num,'\n')

def cmp_n(a,b):
	return (a>b)-(a<b)
a = "3"
b = "20"
print(cmp_n(a,b))

class Solution:
	def largestNum(self,num):
		num = [str(x) for x in num]
		num.sort(cmp=lambda x,y: self.cmp(y+x,x+y))
		largest = "".join(num)
		return largest.lstrip('0') or '0'
		
	def cmp(self, x,y):
		return (x>y) - (x<y)
		
test = Solution()
print(test.largestNum(num))

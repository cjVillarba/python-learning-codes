class Rectangle:
	def __init__(self,w,h):
		self.w = w
		self.h = h
	
	def area(self):
		return self.w*self.h
	
	def perimeter(self):
		return 2*(self.w+self.h)


print('***RECTANGLE***')		
r = Rectangle(3,2)
area = r.area()
print(area)
print(r.perimeter())

class Square(Rectangle):
	def __init__(self,s):
		super(Square,self).__init__(s,s)
		self.s = s

print('***SQUARE***')
s = Square(2)
print(s.area())
print(s.perimeter())
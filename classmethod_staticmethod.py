class D:
	multiplier = 2
	
	@classmethod
	def f(cls,x):
		return cls.multiplier*x
	
	@staticmethod
	def g(name):
		return "Hello %s"%(name)
		
print(D.f)
print(D.f(12))
print("************")
print(D.g)
print(D.g("Charlie The Great!"))

D()

d = D()
d.multiplier = 3
print(d.multiplier)
print(D.multiplier)
print("*************")
print(d.f(2))
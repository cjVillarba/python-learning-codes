#This is the decorator function
def print_args(func):
	def inner_func(*args,**kwargs):
		print(args)
		print(kwargs)
		return func(*args,**kwargs)
	return inner_func

@print_args
def multiply(x,y):
	return x*y

print(multiply(2,3))

#This is a decorator class
class Decorator(object):
	def __init__(self,func):
		self.func = func
		
	def __call__(self,*args,**kwargs):
		print('Before function call')
		res = self.func(*args,**kwargs)
		print('After function call')
		return res

@Decorator
def testfunc():
	print('The function is called')
	
	
testfunc()

print(type(testfunc))
	
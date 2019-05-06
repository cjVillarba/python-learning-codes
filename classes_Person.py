class Person():
	species = 'Homo Sapiens'
	
	def __init__(self, name):
		self.name = name
		
	def rename(self,renamed):
		self.name = renamed
		print('Good {}'.format(self.name))
		return 'I am now %s'%(self.name)
		
	def __str__(self):
		return self.name
		
charlie = Person('Charlie')
print(charlie)
charlie.rename("Charlie the Great")
print(charlie)
print(charlie.species)
print(charlie.rename("Charlie"))

print(Person.rename.__class__)


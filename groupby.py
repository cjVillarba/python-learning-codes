from itertools import groupby
#import itertools
#print(dir(itertools))

things = [('animal','bear'), ('animal','duck'), ('plant','cactus'), ('vehicle','harley'), ('vehicle','speed boat'), ('vehicle','school bus')]

dict = {}
f = lambda x: x[0]
for key, group in groupby(sorted(things,key=f), f):
	dict[key] = list(group)
	
print(dict)
s = lambda x:x*x
print(s(2))
name_len = map(len,["Charlie","Joy","Jules","Gale"])
print(list(name_len))

#Reduce needs to be imported in Python 3+

from functools import reduce

total = reduce(lambda a,x:a+x,[0,1,2,3,4])
print(total)

arr = [0,1,2,3,4,5,6,7]
arr_fil=filter(lambda x:x>4,arr)
print(list(arr_fil))

print([i for i in filter(lambda x:x>5,range(10))])
import heapq
print(dir(heapq))

num = [1,2,3,4,5,6,7,8,9]
print(heapq.nlargest(2,num))

x = [10,4,2,100,20,50,32,200,150,8]
heapq.heapify(x)
print(x)
N,K=map(int,raw_input().split())
list=[int(x) for x in raw_input().split()]
list.sort()
m=list[::-1]
print m[K-1]

n=int(raw_input())
l=[int(x) for x in raw_input().split()]
m=[]
for i in range(0,n):
	m.append(l[i])
for i in range(0,len(l)):
	if(i is m[i]):
		print i,
